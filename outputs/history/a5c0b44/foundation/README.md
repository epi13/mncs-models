# Verification evidence

`native-result.json` is unmodified mncs-test output with compiler-owned inventory,
artifact/run/test identities, native results, and per-test bytecode steps.
`receipt.json` binds source and binary hashes, native result hash, observed tool
checkout heads, source sizes and compilation-plus-suite wall time. Regenerate
both with `python3 scripts/verify.py`; a failed or incomplete suite fails closed.
These are local execution observations, not independent attestation, operational
benefit evidence, calibrated prediction results or a family conformance badge.

The frozen synthetic metrics are asserted in native test
`heldout_model_comparison` and `heldout_deterministic_baselines`. Full numerical
contracts and experiment interpretation are in `docs/NATIVE_FOUNDATION.md`.
