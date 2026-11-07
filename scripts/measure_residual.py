#!/usr/bin/env python3
"""Typed native-call transport: returned numerical values become typed arguments.

No model arithmetic, feature labeling, scoring, fitting, or policy lives here.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
COMMON = Path(subprocess.check_output(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=ROOT, text=True).strip())
FAMILY = COMMON.parent.parent
LANG = Path(os.environ.get("MNCS_LANGUAGE_DIR", FAMILY / "mncs-language"))
TEST = Path(os.environ.get("MNCS_TEST_DIR", FAMILY / "mncs-test"))
BIN = Path(os.environ.get("MNCS_BIN", LANG / "target/debug/mncs"))
OUT = ROOT / "outputs/residual"
OUT.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MNCS_NATIVE_APPLICATION_CACHE_DIR", str(COMMON / "mncs-native-application-cache" / hashlib.sha256(str(BIN.resolve()).encode()).hexdigest()[:16]))
LIBRARIES = ["--library", "src", "--library", "tests/fixtures", "--library", str(TEST / "native"), "--library", str(LANG / "library")]

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def sources():
    return {str(p.relative_to(ROOT)): digest(p) for p in sorted(ROOT.rglob("*.mncs")) if p.is_file()}

initial = sources()
binary = digest(BIN)
measurements = {}

def host_value(value):
    """Adapt compiler return tuples to its documented HostExecutionValue maps.

    Numeric/boolean data and variant names are unchanged; declared native ABI
    types validate every nested field. This is wire-format conversion only.
    """
    if "record" in value:
        return {"record": {"fields": {name: host_value(cell) for name, cell in value["record"]["fields"]}}}
    if "finite_variant" in value or "finite" in value:
        finite = value.get("finite_variant", value.get("finite"))
        return {"finite": {"variant": finite["variant_identity"].split("::")[-1]}}
    if "finite_payload" in value:
        finite = value["finite_payload"]
        return {"finite": {"variant": finite["variant_identity"].split("::")[-1], "payload": {name: host_value(cell) for name, cell in finite["fields"]}}}
    if "sequence" in value:
        return {"sequence": {"values": [host_value(cell) for cell in value["sequence"]["values"]]}}
    for kind in ["integer", "boolean", "byte", "float"]:
        if kind in value:
            return {kind: {"value": value[kind]["value"]}}
    raise ValueError("Unsupported compiler transport value")

def call(function, arguments=(), label=None):
    label = label or function
    argument_path = OUT / (label + ".args.json")
    result_path = OUT / (label + ".json")
    argument_path.write_text(json.dumps([host_value(value) for value in arguments], indent=2) + "\n")
    result_path.unlink(missing_ok=True)
    command = [str(BIN), "call", "tests/native/residual.mncs", "--module", "mncs.models.residual_tests", "--function", function, "--args", str(argument_path), *LIBRARIES, "--step-budget", "3000000", "--result", str(result_path)]
    start = time.monotonic()
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=180)
    wall = time.monotonic() - start
    if proc.returncode or not result_path.is_file():
        raise SystemExit(proc.stderr + proc.stdout)
    data = json.loads(result_path.read_text())
    if data.get("status") != "returned" or data.get("call", {}).get("status") != "returned":
        raise SystemExit(f"Native call failed: {label}")
    measurements[label] = {"function": function, "vm_steps": data["call"]["steps"], "wall_seconds": wall, "wall_scope": "CLI admission/compile-cache access, typed transport and execution; not inference-only latency", "arguments_sha256": digest(argument_path), "result_sha256": digest(result_path)}
    print(label, data["call"]["steps"], flush=True)
    return data["call"]["returned"][0]

(OUT / "stages.json").unlink(missing_ok=True)
model = call("five")
raw = call("raw_five")
signal = call("signal_fixture")
xs = call("inputs_fixture")
call("validate_candidate", [raw], "validate_100")
call("validate_candidate", [model], "validate_5")
call("cold_infer", [raw, signal], "infer_100")
call("cold_infer", [model, signal], "infer_5")
call("four_calls", [model, xs])
call("lexical_four", [model, xs])
edited = call("revision_probe", [model])
# Field selection is transport, not a learned decision or parameter edit.
updated = dict(edited["record"]["fields"])["model"]
call("validate_candidate", [updated], "revalidate_edit")
graph = call("packed_graph")
call("validate_graph", [graph])
call("cold_graph", [graph])
sensors = call("packed_sensors")
call("full_sensor", [sensors])
call("projected_sensor", [sensors])
call("four_projected", [sensors])
call("batched_sensor", [sensors])
call("resolved_gate_probe")
call("candidate_gate_probe")
call("candidate_prediction_probe", [model])
# Direct numerical interchange: identical code/artifact, two supplied weight sets.
integer = lambda n: {"integer": {"type": {"bits": 64, "signed": True}, "value": n}}
sequence = lambda values: {"sequence": {"values": [integer(n) for n in values]}}
for label, weights in [("authored_initial", [3, 1, 1, 1, -6]), ("authored_revision", [3, 1, 3, 1, -6])]:
    argument_path = OUT / (label + ".args.json")
    argument_path.write_text(json.dumps([sequence(weights), sequence([2, 1, 2, 0])], indent=2) + "\n")
    command = [str(BIN), "call", "src/models/trial.mncs", "--module", "mncs.models.trial", "--function", "score_authored", "--args", str(argument_path), *LIBRARIES, "--result", str(OUT / (label + ".json"))]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=180)
    if proc.returncode:
        raise SystemExit(proc.stderr + proc.stdout)
    measurements[label] = {"arguments_sha256": digest(argument_path), "result_sha256": digest(OUT / (label + ".json")), "scope": "mechanical parameter interchange only, not a controlled LLM trial"}
if sources() != initial or digest(BIN) != binary:
    raise SystemExit("Source or compiler changed during stage measurement")
(OUT / "stages.json").write_text(json.dumps({"schema": "mncs.models.stage-measurements/1", "source_sha256": initial, "compiler_binary_sha256": binary, "measurements": measurements, "limitations": ["VM steps exclude CLI transport/compilation; wall time includes them", "Returned value data are preserved through tuple-to-map ABI conversion; each standalone call revalidates admission", "Reuse without revalidation occurs only inside the native lexical batch", "No operational savings or controlled LLM authoring efficiency measured"]}, indent=2) + "\n")
