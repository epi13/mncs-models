#!/usr/bin/env python3
"""Verification transport and receipt packaging; all model/evaluation semantics are MNCS."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
COMMON = Path(subprocess.check_output(
    ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=ROOT, text=True).strip())
FAMILY = COMMON.parent.parent
LANG = Path(os.environ.get("MNCS_LANGUAGE_DIR", FAMILY / "mncs-language"))
TEST = Path(os.environ.get("MNCS_TEST_DIR", FAMILY / "mncs-test"))
BIN = Path(os.environ.get("MNCS_BIN", LANG / "target/debug/mncs"))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def sources():
    return {str(p.relative_to(ROOT)): digest(p) for p in sorted(ROOT.rglob("*.mncs")) if p.is_file()}

def revision(path):
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path, text=True).strip()

parser = argparse.ArgumentParser()
parser.add_argument("--output-root", default="outputs", help="Separate evidence directory; preserve previous receipts")
parser.add_argument("--suite", choices=["all", "foundation", "composition", "residual", "guidance", "replay", "feasibility"], default="all")
args = parser.parse_args()
libraries = ["--library", "src", "--library", "experiments/first_guidance", "--library", "tests/fixtures", "--library", str(TEST / "native"), "--library", str(LANG / "library")]
# Match the native Test tool's shared, toolchain-scoped cache convention.
cache_scope = hashlib.sha256(str(BIN.resolve()).encode()).hexdigest()[:16]
os.environ.setdefault("MNCS_NATIVE_APPLICATION_CACHE_DIR", str(COMMON / "mncs-native-application-cache" / cache_scope))
source_hashes = sources()
binary_hash = digest(BIN)
verification_started_at_unix_ms = time.time_ns() // 1000000
for suite, minimum in [("foundation", 14), ("composition", 16), ("residual", 15), ("guidance", 26), ("replay", 15), ("feasibility", 5)]:
    if args.suite not in ("all", suite):
        continue
    out = ROOT / args.output_root / suite
    out.mkdir(parents=True, exist_ok=True)
    result = out / "native-result.json"
    receipt_path = out / "receipt.json"
    # Invalidate stale successful evidence before beginning a new attempt.
    receipt_path.unlink(missing_ok=True)
    result.unlink(missing_ok=True)
    command = [str(BIN), "test", f"tests/native/{suite}.mncs", *libraries,
               "--step-budget", "3000000", "--format", "text", "--result", str(result)]
    suite_started_at_unix_ms = time.time_ns() // 1000000
    start = time.monotonic()
    run = subprocess.run(command, cwd=ROOT, timeout=180)
    elapsed = time.monotonic() - start
    suite_finished_at_unix_ms = time.time_ns() // 1000000
    if run.returncode or not result.is_file():
        raise SystemExit(run.returncode or 1)
    data = json.loads(result.read_text())
    if data.get("summary", {}).get("verdict") != "PASS" or data["summary"].get("total", 0) < minimum:
        raise SystemExit("Native suite incomplete or failed")
    measurements = {}
    if suite == "composition":
        for function in ["benchmark", "composed_cost", "standalone_cost", "deterministic_cost", "scale_cost", "subset_cost"]:
            path = out / f"{function}.json"
            path.unlink(missing_ok=True)
            call = [str(BIN), "call", "tests/native/composition.mncs", "--module", "mncs.models.composition_tests", "--function", function, "--args-json", "[]", *libraries, "--step-budget", "3000000", "--result", str(path)]
            called = subprocess.run(call, cwd=ROOT, capture_output=True, text=True, timeout=180)
            if called.returncode or not path.is_file():
                raise SystemExit(called.stderr + called.stdout)
            observation = json.loads(path.read_text())
            if observation.get("status") != "returned" or observation.get("call", {}).get("status") != "returned":
                raise SystemExit(f"Native measurement failed: {function}")
            measurements[function] = {"sha256": digest(path), "steps": observation["call"]["steps"]}
    if suite == "guidance":
        for function in ["demand_cost", "one_cost", "pair_cost", "eight_cost", "bypass_cost", "partial_workflow"]:
            path = out / f"{function}.json"
            path.unlink(missing_ok=True)
            call = [str(BIN), "call", "tests/native/guidance.mncs", "--module", "mncs.models.guidance_tests", "--function", function, "--args-json", "[]", *libraries, "--step-budget", "3000000", "--result", str(path)]
            start_call = time.monotonic()
            called = subprocess.run(call, cwd=ROOT, capture_output=True, text=True, timeout=180)
            wall_call = time.monotonic() - start_call
            if called.returncode or not path.is_file():
                raise SystemExit(called.stderr + called.stdout)
            observation = json.loads(path.read_text())
            if observation.get("status") != "returned" or observation.get("call", {}).get("status") != "returned":
                raise SystemExit(f"Native measurement failed: {function}")
            measurements[function] = {"sha256": digest(path), "steps": observation["call"]["steps"], "wall_seconds": wall_call, "scope": "complete native invocation including fixture construction; wall includes CLI compilation/cache/transport"}
    if suite == "composition":
        pressure = out / "compact-view-refusal.json"
        refusal = subprocess.run([str(BIN), "test", "tests/pressures/compact_view_refusal.mncs", *libraries, "--format", "json"], cwd=ROOT, capture_output=True, text=True, timeout=60)
        refused = json.loads(refusal.stdout)
        if refusal.returncode == 0 or "MNE198" not in json.dumps(refused.get("failure", {})):
            raise SystemExit("Expected native view-update refusal was not reproduced")
        pressure.write_text(json.dumps(refused, indent=2) + "\n")
        measurements["compact_view_update"] = {"sha256": digest(pressure), "status": "expected_refusal", "diagnostic": "MNE198"}
    if sources() != source_hashes or digest(BIN) != binary_hash:
        raise SystemExit("Source or compiler changed during verification")
    receipt = {
        "schema": "mncs.models.verification-evidence/1", "suite": suite,
        "boundary": "native bounded models, DAGs, residual and operation-guidance contracts; mechanical verification only; activity audit is observational, not predictive utility; no operational integration or family conformance claim",
        "result_sha256": digest(result), "native_run_id": data["run_id"],
        "summary": data["summary"], "execution": data["execution"],
        "suite_wall_seconds": elapsed, "wall_scope": "compilation and suite, not inference-only latency",
        "verification_started_at_unix_ms": verification_started_at_unix_ms,
        "suite_started_at_unix_ms": suite_started_at_unix_ms,
        "suite_finished_at_unix_ms": suite_finished_at_unix_ms,
        "chronology_scope": "Host clock observations, not authenticated custody or an independent clock attestation",
        "source_sha256": source_hashes, "compiler_binary_sha256": binary_hash,
        "observed_language_checkout": revision(LANG), "observed_test_checkout": revision(TEST),
        "checkout_revision_note": "Observed heads are not binary build attestations; the binary hash binds execution.",
        "measurements": measurements,
        "source_artifact_bytes": {str(p.relative_to(ROOT)): p.stat().st_size for p in sorted((ROOT / "src").rglob("*.mncs"))},
    }
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"Verified {data['summary']['total']} native {suite} tests; receipt: {receipt_path}")
