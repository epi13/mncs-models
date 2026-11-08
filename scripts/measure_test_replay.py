#!/usr/bin/env python3
"""Prepare a pre-decision snapshot, then transport complete native Test outcomes.

No fitting, model arithmetic, outcome invention, or host selection/evaluation.
Run --prepare before verify.py; --evaluate afterward. This is an exploratory
eligibility replay, not a sealed author/reviewer trial or a telemetry collector.
"""
import argparse
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
OUT = ROOT / "outputs/decision-trial"
SUITES = ["foundation", "composition", "residual", "guidance"]
os.environ.setdefault("MNCS_NATIVE_APPLICATION_CACHE_DIR", str(COMMON / "mncs-native-application-cache" / hashlib.sha256(str(BIN.resolve()).encode()).hexdigest()[:16]))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources():
    return {str(p.relative_to(ROOT)): digest(p) for p in sorted(ROOT.rglob("*.mncs")) if p.is_file()}


def dependencies():
    return {str(p.relative_to(FAMILY)): digest(p) for base in [TEST / "native", LANG / "library"] for p in sorted(base.rglob("*.mncs")) if p.is_file()}


def write(name, value):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    return path


def number(x):
    return {"integer": {"value": x}}


def record(**fields):
    return {"record": {"fields": fields}}


def sequence(values):
    return {"sequence": {"values": values}}


def variant(name):
    return {"finite": {"variant": name}}


def boolean(value):
    return {"boolean": {"value": value}}


def call(module, function, arguments, label):
    args_path = write(f"replay/{label}.args.json", arguments)
    result_path = OUT / f"replay/{label}.json"
    result_path.unlink(missing_ok=True)
    command = [str(BIN), "call", f"src/models/{module}.mncs", "--module", f"mncs.models.{module}", "--function", function, "--args", str(args_path), "--library", "src", "--library", str(LANG / "library"), "--step-budget", "3000000", "--result", str(result_path)]
    start = time.monotonic()
    run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=180)
    wall = time.monotonic() - start
    if run.returncode or not result_path.is_file():
        raise SystemExit(run.stderr + run.stdout)
    response = json.loads(result_path.read_text())
    if response.get("status") != "returned" or response.get("call", {}).get("status") != "returned":
        raise SystemExit(f"Native call failed: {label}")
    return {"arguments_sha256": digest(args_path), "result_sha256": digest(result_path), "vm_steps": response["call"]["steps"], "cli_wall_seconds": wall, "scope": "CLI admission/cache, typed transport and native evaluation; not inference-only latency"}


def native_suite(base, suite):
    receipt_path = base / suite / "receipt.json"
    result_path = base / suite / "native-result.json"
    receipt = json.loads(receipt_path.read_text())
    result = json.loads(result_path.read_text())
    if receipt["result_sha256"] != digest(result_path):
        raise SystemExit(f"Receipt mismatch: {suite}")
    execution = result["execution"]
    if not execution["canonical_path"] or execution["fallback"] or execution["host_subprocesses"]:
        raise SystemExit(f"Unsupported execution: {suite}")
    summary = result["native_suite_summary"]
    for key in ["compile_failures", "runtime_failures", "infrastructure_failures", "setup_failures", "timeout_failures", "unsupported", "skipped"]:
        if summary[key]:
            raise SystemExit(f"Non-assertion/unknown outcome requires owner review: {suite}, {key}")
    if result["summary"]["authority"] != "native_suite" or summary["verdict"] not in {"PASS", "FAIL"}:
        raise SystemExit(f"Missing native assertion verdict: {suite}")
    if any(t["execution"]["status"] != "returned" or t["native_result"].get("authority") != "native_suite" for t in result["tests"]):
        raise SystemExit(f"Incomplete native assertions: {suite}")
    # Aggregation of owner-measured counters, not predicted cost or utility.
    steps = sum(t["execution"]["steps"] for t in result["tests"])
    return receipt, result, steps, {"receipt_sha256": digest(receipt_path), "result_sha256": digest(result_path), "native_run_id": result["run_id"], "execution": execution, "selection": result["selection"], "summary": result["summary"], "vm_steps": steps, "suite_wall_seconds": receipt["suite_wall_seconds"]}


parser = argparse.ArgumentParser()
parser.add_argument("--prepare", action="store_true")
parser.add_argument("--evaluate", action="store_true")
parser.add_argument("--output-root", default="outputs/decision-trial", help="Study directory containing baseline/ and verification/; existing plans are immutable")
args = parser.parse_args()
OUT = ROOT / args.output_root
if args.prepare == args.evaluate:
    raise SystemExit("Choose exactly one of --prepare or --evaluate")

if args.prepare:
    if (OUT / "plan.json").exists():
        raise SystemExit("Plan already exists; preserve it and use a new output campaign for another trial")
    start = time.monotonic()
    source_hashes, dependency_hashes, binary_hash = sources(), dependencies(), digest(BIN)
    prior, cs = {}, []
    # These baseline executions exist before this decision; no final outcomes
    # enter the problem or its baseline call.
    for op, suite in enumerate(SUITES, 1):
        receipt, result, cost, observation = native_suite(OUT / "baseline", suite)
        prior[suite] = observation
        cs.append((op, cost))
    available_at = time.time_ns() // 1000000
    acquisition = time.monotonic() - start
    boundary = record(**{k: number(v) for k, v in dict(event=1001, question=601, state=201, decision_at=available_at, established_reference=602, permitted_reference=603, operation_contract=604, resolved_operation=0).items()})
    candidates = [record(operation=number(op), contract=number(604), evidence=record(event=number(1001), state=number(201), reference=number(800 + op), authority=number(301), available_at=number(available_at), status=variant("Present")), ready=boolean(True), cost_known=boolean(True), cost=number(cost)) for op, cost in cs]
    problem = record(boundary=boundary, candidates=sequence(candidates), ranking_reference=number(605), cost_unit=number(606), max_candidates=number(8), max_operation_cost=number(3000000))
    plan = {"schema": "mncs.models.test-priority-plan/1", "status": "exploratory-eligibility-replay-no-model-or-heldout", "decision_at_unix_ms": available_at, "chronology": "Host observations, not independent clock/custody attestation", "feature_acquisition_wall_seconds": acquisition, "feature_acquisition_scope": "Read/hash native sources, dependencies, compiler and four prior receipts/results; excludes Environment entry/Store and native baseline call", "source_sha256": source_hashes, "dependency_sha256": dependency_hashes, "compiler_binary_sha256": binary_hash, "operations": {str(i): s for i, s in enumerate(SUITES, 1)}, "references": {"1000": "this exact source/dependency/compiler snapshot", "602": "source inventory and eligibility analysis; not an established best operation", "603": "exact four-suite permitted snapshot in problem", "604": "canonical native Test suite execution", "605": "existing guide_operations unique least prior VM cost", "606": "sum of owner-reported per-test VM steps; excludes compilation/admission", "301": "native Test assertion authority; handles require external source binding"}, "prior": prior, "problem": problem, "source_state_count": 1, "heldout_sealed": False, "model_invocations": 0}
    write("plan.json", plan)
    measurement = call("guidance", "guide_operations", [problem], "predecision-baseline")
    write("baseline-call.json", measurement)
    if sources() != source_hashes or dependencies() != dependency_hashes or digest(BIN) != binary_hash:
        raise SystemExit("Inputs changed during preparation; plan is invalid")
    print("Prepared source-bound plan and native deterministic baseline; no final outcomes read")
else:
    if (OUT / "replay-receipt.json").exists():
        raise SystemExit("Replay already recorded; preserve its results and use a new output campaign")
    plan = json.loads((OUT / "plan.json").read_text())
    if sources() != plan["source_sha256"] or dependencies() != plan["dependency_sha256"] or digest(BIN) != plan["compiler_binary_sha256"]:
        raise SystemExit("Frozen source, dependencies or compiler changed")
    rows, observations = [], {}
    for op, suite in enumerate(SUITES, 1):
        receipt, result, cost, observation = native_suite(OUT / "verification", suite)
        if receipt["source_sha256"] != plan["source_sha256"] or receipt["compiler_binary_sha256"] != plan["compiler_binary_sha256"] or receipt["suite_started_at_unix_ms"] <= plan["decision_at_unix_ms"]:
            raise SystemExit(f"Source/chronology mismatch: {suite}")
        observations[suite] = observation
        rows.append(record(**{k: number(v) for k, v in dict(event=1001, question=601, state=201, operation=op, permitted_reference=603, source_reference=1000, reference=900 + op, authority=301, observed_at=receipt["suite_finished_at_unix_ms"], cost_unit=606, cost=cost).items()}, kind=variant("Observed"), verdict=variant({"PASS": "Passed", "FAIL": "Failed"}[result["native_suite_summary"]["verdict"]]), cost_known=boolean(True)))
    calls = {}
    for op in range(5):
        calls[str(op)] = call("trial", "evaluate_initial_test", [plan["problem"], number(1000), sequence(rows), number(op)], f"first-{op}")
    calls["missing-alternatives"] = call("trial", "evaluate_initial_test", [plan["problem"], number(1000), sequence(rows[:1]), number(1)], "missing-alternatives")
    if sources() != plan["source_sha256"] or dependencies() != plan["dependency_sha256"] or digest(BIN) != plan["compiler_binary_sha256"]:
        raise SystemExit("Frozen inputs changed during evaluation")
    write("replay-receipt.json", {"schema": "mncs.models.test-priority-replay/1", "plan_sha256": digest(OUT / "plan.json"), "calls": calls, "outcomes": observations, "row_references": {str(900 + op): {"operation": op, "native_result": f"verification/{suite}/native-result.json", "result_sha256": observations[suite]["result_sha256"]} for op, suite in enumerate(SUITES, 1)}, "model_invocations": 0, "controlled_weight_trial": "not-conducted-no-eligible-cohort", "utility_scope": "first native assertion failure only; no causal productivity or saved required executions"})
    print("Native complete-outcome replay recorded; abstention and missing alternatives retained")
