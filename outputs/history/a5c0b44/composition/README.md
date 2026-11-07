# Native composition evidence

Regenerate with `python3 scripts/verify.py --suite composition`.

- `native-result.json`: sixteen native tests, with compiler inventory, artifact/run/test identities and VM execution steps.
- `benchmark.json`: unmodified native callable result for the frozen 32-event synthetic comparison.
- `*_cost.json`: native cost probes including construction and validation, not isolated inference latency.
- `compact-view-refusal.json`: expected compiler refusal MNE198 for immutable update on a bounded view.
- `receipt.json`: source/binary/result/measurement hashes, source sizes and compilation-plus-suite wall time.

The original fourteen tests and prior experiment remain under `outputs/foundation/`.
The compact-view refusal is an observed limitation, not a successful executable model test.
All benchmark labels are synthetic; no operational benefit, calibrated uncertainty,
independent attestation, or family conformance is claimed. See `docs/COMPOSITION.md`.
