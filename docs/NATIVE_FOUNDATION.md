# Native micro-model foundation

Implemented contract: [RFC 0002](../rfcs/0002-native-micro-models.md).
The broader graph vocabulary in ARCHITECTURE.md remains a design direction.
The executable boundary is intentionally a small serial dense composition,
not the whole graph charter. MNEL is historical, not an authority here.

## Run and author

From this repository run `python3 scripts/verify.py`. It uses the sibling
`mncs-language/target/debug/mncs`, `mncs-test/native`, and language library.
Set `MNCS_BIN`, `MNCS_LANGUAGE_DIR`, or `MNCS_TEST_DIR` for other admitted
installations. No automatic compiler build, package installation, ML runtime,
external service, or network inference is required. The Python file only invokes
mncs-test, checks its verdict, and hashes evidence; every model operation and
experimental evaluation executes in MNCS.

Import `mncs.models.micro` from library root `src`. Construct a `Topology`,
`Parameters`, and `Model` record, then call `model_valid` and `infer`.
`authored()` in tests/native/foundation.mncs is a complete five-parameter example.
Supply all 100 parameter slots, zeroing unused slots (array fill plus native
`replace` is convenient). Layer rows contain input weights then bias; the second
layer starts after `(inputs + 1) * hidden`. Hidden width zero means one layer.
`relu` controls the first layer; a second layer has identity activation.
Inputs/outputs use `Signal` with eight slots and an explicit active width.

For revision, call `edit(model, index, value, new_revision, provenance_ref)`.
An accepted edit returns a new model with unchanged topology, one replaced
parameter, new provenance, and a parent revision; refusal returns the original.
The original remains usable for rollback. Initial construction supplies five active
slots; the demonstrated modification changes one slot. Both validation and edits
scan the bounded 100-slot array; agent tokens and construction wall cost were not
measured. `changes(a,b)` counts differing slots;
compare topology fields separately before interpreting that count as a revision
diff. Records expose every parameter and dimension for inspection. Parameters
are values passed to inference: changing them does not require recompiling the
inference implementation. The test fixtures embed construction values in source
for reproducibility, not as a restriction on parameter origin. A production
serialized-artifact loader is not implemented; ingress/storage own that boundary.

## Numerical and resource contract

All lanes are scale-one i64. This is a deliberate exact arithmetic domain,
not a claim that MNCS lacks floating point: Profile 0.12 supports finite f64,
but its float sequence restrictions make integer arrays sufficient for this slice.
Dimensions are 1..8, optional hidden 1..8, and at most 100 active parameters.
Weights and biases are -100..100; inputs -1000..1000. Unused slots must be zero.
Validation precedes indexing or arithmetic based on supplied dimensions.
Worst first-layer magnitude is 800100; worst second-layer magnitude is
640080100, safely inside i64. Arithmetic never silently saturates, quantizes,
wraps, or converts a missing value to a valid zero input.

`Inference.status` is 0 success, 1 invalid model, 2 invalid input. Refusals have
zero-width output and zero operation counts. Reported multiply/add counts are
active mathematical operations, not VM instructions or wall time. A five-parameter
4-to-1 model uses four multiplies and four additions (bias seeds accumulation).
The bounded implementation also traverses padded arrays: validation scans 100
parameter slots, input validation eight, each layer eight output slots and each
active row eight input slots. These overheads matter for tiny models.

Active numerical parameter payload is `8 * parameter_count` bytes (40 for the
experiment); the fixed parameter array occupies 800 logical bytes regardless of
active count. Each signal has 64 logical lane bytes plus width. This is not a
measurement of stack, compiler arena, process RSS, ABI padding, or peak memory.
The receipt records actual source artifact bytes, suite wall time, binary digest,
native artifact identity, and source hashes. Native-result.json records measured
VM steps per test (which include construction, validation and assertions).
Inference-only latency, peak memory, energy, and environmental savings remain
unmeasured. Do not equate MAC counts with total execution cost.

## Reproducible experiment

All fixtures are synthetic, independently authored plausible diagnostic scenarios;
no historical traces, operational outcomes, or real resource observations were
used. Features are signature severity, repetition, pressure, and unhealthy signal.
The target is whether additional diagnosis would be useful. Labels are synthetic
verified outcomes supplied by the fixture author, not model predictions.

Construction events 1..4 are the four cases in `construction_cases`; tuning events
11..12 are the pressure-positive and negative cases in
`tuning_and_construction_regression`. Held-out event groups 101..108 are explicit
records in `heldout`. The held-out cases were not used to choose the parameters;
tests assert frozen results and must not become a tuning feedback loop. This tiny
hand-authored split proves the procedure, not statistical generalization or LLM
superiority over optimization. For real traces use chronological/event-grouped
splits and seal test evidence before construction.

The initial model is `[3, 1, 1, 1, -6]`; tuning changes index 2 to 3.
No hidden layer is necessary. Construction and tuning regressions are checked.
The single-view ablation sets both Doctor weights to zero while keeping the same
input/provenance contract; it is not independently optimized.

| Frozen held-out method | Strict correct / 8 | Abstentions | False positives | False negatives |
| --- | ---: | ---: | ---: | ---: |
| Signature-only deterministic threshold >= 2 | 4 | 0 | 1 | 3 |
| Initial directly authored model | 4 | 1 | 1 | 2 |
| Modified dual-view model | 7 | 0 | 1 | 0 |
| Forge-only parameter ablation | 4 | 0 | 1 | 3 |
| Informed deterministic rule: signature >= 3 or pressure >= 2 | 8 | 0 | 0 | 0 |

Abstentions count as incorrect in strict accuracy. Missing or contradictory inputs
are separately tested and are not counted as healthy negative cases. Scores in
[-1,1] abstain; scores above 1 suggest useful diagnostics, below -1 suggest not
useful. Scores are not calibrated probabilities. The informed rule fully expresses
the synthetic labeling relationship: prefer it here. The experiment demonstrates
multiview feature fusion and edit/evaluation mechanics, not predictive representation
learning, learned embeddings, causal discovery, or deployment benefit. No training
baseline is added: learning/optimization belongs to mncs-learn; a future small
native bounded optimizer comparison should use the identical frozen split.

## Complementary views and authority

`views.mncs` provides nominal ForgeView and DoctorView records with independent
source evidence references, availability/contradiction flags and matching event
identities. Neither source is made subordinate to a model. `Prediction` preserves
both references, event, model identity and parameter revision. Unavailability, contradiction, invalid
inference and margin abstention have distinct status codes. Contradiction flags
must come from the caller's evidence assessment: this module cannot discover all
semantic conflicts between sources. Evidence references are opaque references,
not authenticated custody or rights checks. Consumers must bind them to their
existing provenance authority and verified event projection.

These records are illustrative model input contracts, not Forge/Doctor wire APIs.
No operational adapters or changes to either tool were made. Forge owns execution
and receipts; Doctor owns health diagnosis; Fabric owns worker admission and
placement; RAVEL owns evidence selection; Environment owns claims, readiness and
lifecycle. They may eventually project stable bounded features into these ports.
A prediction has no effects, grants, recovery action, escalation authority, or
verified-outcome status. Consumers can bypass it and retain deterministic behavior.

## Reconnaissance and current limits

The committed repository was a documentation-first scaffold. The older checkout
on `models-foundation` contains untracked graph/reference experiments, including
an integer graph executor and Python oracle. Those files were inspected as
historical work and preserved in place; none were adopted or overwritten.
This phase starts from committed main in a linked worktree and adds no host model
implementation. Apache-2.0 applies; no external code, parameters or datasets were
imported. Existing rights/provenance policy remains with its owner.

Observed source heads: language f8212ed, Commons c53ae0b, learn 24f4d25,
memory 601cbca, ingest c07cfbc, store 4358df4, rights 9f4a625,
Actions 8517267, Forge e1d5998, Doctor 80afe6f, Fabric c464863,
RAVEL e1cae6d. These are reconnaissance observations, not dependency pins.
The receipt binds the compiler actually executed by binary hash; checkout HEAD
alone is not evidence that a prebuilt binary was built from those exact sources.
Native tests use compiler inventory and the canonical mncs-test bytecode path,
without fallback or host subprocess inference. No cross-backend agreement or
family conformance is claimed.

Environment MCP entry rejected the old checkout because it lacks the repository
manifest required by current registration. An independent local read-only
orientation session (`ses_93412bbc8dac36a8`) entered the isolated worktree and
its repository claim query found only released claims. Current-working-checkout
mutation entry also refuses because Environment verifies the primary checkout's
manifest; it additionally exposes a duplicate `code` diagnostic exception in its
error path. This is a precise Environment integration limitation, not a numerical
or language blocker. No foreign checkout or Environment code was changed to
circumvent it. Workspace user authorization governs the isolated Git delivery;
no Environment mutation verification is claimed.

Implemented: bounded dense composition, topology/parameter/input validation,
identity and lineage references, inference, immutable parameter edits, operation
counts, typed evidence fusion, refusal/abstention, native evaluation and receipts.
Conceptual: arbitrary graphs, parameter aliasing, recurrence, routing, learned
encoders, automated discovery, serialization/store binding, authenticated source
lineage, calibration, drift detection, training, deployment and operational savings.
There is no new registry, orchestration service, or authority boundary.

Next work should choose one real narrow uncertainty with authorized event-aligned
traces; freeze an evaluation split; compare strong deterministic baselines; measure
full invocation overhead and avoided work. Bind source/model digests and revisions
to existing Store/rights contracts, and let mncs-learn propose governed updates.
Only add another primitive or numeric representation when that experiment needs it.
