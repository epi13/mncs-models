#!/usr/bin/env python3
"""Transport only: invoke native mncs-test and retain source-bound evidence."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
# Linked worktrees resolve tool dependencies through the owning Git family.
COMMON = Path(subprocess.check_output(
    ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=ROOT, text=True).strip())
FAMILY = COMMON.parent.parent
LANG = Path(os.environ.get("MNCS_LANGUAGE_DIR", FAMILY / "mncs-language"))
TEST = Path(os.environ.get("MNCS_TEST_DIR", FAMILY / "mncs-test"))
BIN = Path(os.environ.get("MNCS_BIN", LANG / "target/debug/mncs"))
OUT = ROOT / "outputs/foundation"
OUT.mkdir(parents=True, exist_ok=True)
result = OUT / "native-result.json"
result.unlink(missing_ok=True)
command = [str(BIN), "test", "tests/native/foundation.mncs", "--library", "src",
           "--library", str(TEST / "native"), "--library", str(LANG / "library"),
           "--format", "text", "--result", str(result)]
start = time.monotonic()
run = subprocess.run(command, cwd=ROOT, timeout=120)
elapsed = time.monotonic() - start
if run.returncode or not result.is_file():
    raise SystemExit(run.returncode or 1)
data = json.loads(result.read_text())
if data.get("summary", {}).get("verdict") != "PASS" or data["summary"].get("total", 0) < 14:
    raise SystemExit("Native suite incomplete or failed")
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def revision(path):
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path, text=True).strip()
receipt = {
    "schema": "mncs.models.foundation-evidence/1",
    "boundary": "native bounded dense inference and synthetic multiview experiment; no operational integration or MNCS conformance claim",
    "result_sha256": digest(result),
    "native_run_id": data["run_id"], "summary": data["summary"],
    "execution": data["execution"],
    "suite_wall_seconds": elapsed,
    "wall_scope": "compilation plus native suite; not per-inference latency",
    "source_sha256": {str(p.relative_to(ROOT)): digest(p) for p in sorted(ROOT.rglob("*.mncs")) if p.is_file()},
    "compiler_binary_sha256": digest(BIN),
    "observed_language_checkout": revision(LANG),
    "observed_test_checkout": revision(TEST),
    "checkout_revision_note": "Observed source heads are not a build attestation for the binary; binary digest and native artifact identity bind this execution.",
    "source_artifact_bytes": {str(p.relative_to(ROOT)): p.stat().st_size for p in sorted((ROOT / "src").rglob("*.mncs"))},
}
(OUT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(f"Verified {data['summary']['total']} native tests; receipt: {OUT / 'receipt.json'}")
