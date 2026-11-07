# RFC 0002 — Bounded native micro-model execution

Status: implemented experimental slice of RFC 0001.

## Decision and invariant

Proportional learned intelligence begins with an inspectable serial composition of
one or two dense affine transforms, optional first-layer ReLU, and separately
bound numerical parameters. The representation does not encode parameter origin.
A caller can author, optimize, store or replace the same Parameters value.
Construction and mutation do not imply permission to promote a revision.

The canonical implementation is `src/models/micro.mncs`. It uses supported Source
Profile 0.18 records, exact i64 arrays, bounded iteration, conditionals and replace.
There is no host semantic implementation. `views.mncs` is a bounded illustrative
input/output contract over that implementation. Tests and experimental evaluation
are native; the Python verification launcher is transport and evidence packaging.

## Primitive contract

Dense transform purpose: weighted relationships and tiny neural compositions.
Inputs/outputs: explicit 1..8 lane dimensions, optional hidden dimension, immutable
signals. Stateflow: no persistent or recurrent state. Parameter ownership: a caller
supplies packed output-row weights and biases separately from Topology. A second
transform consumes the first's output only when hidden width is nonzero. ReLU is
explicit; final two-layer output is identity. Static aspects are topology and
numerical envelope; parameter values and input signals are invocation data.

Parameter addresses are zero-based slots in a stable row layout. Edits preserve
structure, validate bounds and padding, and record parent revision plus opaque
provenance reference. Sharing is limited to reusing the same Parameters value
across invocations; graph aliases and recurrent sharing are not implemented.
Structural inspection uses Topology fields; model identity and provenance refs are
caller-owned nonzero handles, not cryptographic content identities. Native compiler
identities and the verification receipt bind source/artifacts. Consumers needing
durable artifact identities must bind existing Store/rights identities to handles;
no competing identity registry or private hash algorithm is introduced.

Execution requires only the current MNCS toolchain and bounded i64 arithmetic.
Scheduling/device placement remains outside model semantics. Failure conditions:
invalid dimensions/parameter count, nonzero padding, missing identity/provenance,
invalid parameter/input bounds or widths, invalid edit address/revision. No
out-of-bounds indexing or arithmetic with unvalidated dimensions is permitted.
Full bounds and layout are specified in docs/NATIVE_FOUNDATION.md.

Reference constructions: a five-parameter diagnostic relationship predictor and a
two-layer ReLU neural witness. A 100-parameter valid topology and maximum numerical
magnitude are exercised. Complementary views fuse deterministic features; no
encoder training, JEPA machinery or predictive-representation claim is involved.

## Verification and integration impact

Native tests cover accepted/refused edits, topology and parameter compatibility,
exact inference, numerical/resource envelopes, missing/contradictory evidence,
abstention, separate construction/tuning/held-out fixtures and regression.
Only mncs-models changes. No operational consumer of this contract existed in
committed main, so no consumer migration is needed. The foreign untracked graph
experiment is preserved, not adopted as a second canonical implementation.
Future work expands this canonical representation when measured pressure warrants
it; the broad RFC 0001 graph, sharing, recurrence and routing obligations remain
unfulfilled, not silently declared verified.

## Trust, alternatives and unresolved work

Predictions never become authoritative state, permission, recovery or verified
outcome. Uncalibrated scores are labeled as such. The proving ground compares both
weak and informed deterministic rules, and favors the informed rule on this data.
A full graph runtime, embedding framework or host ML dependency would enlarge
maintenance and conversion costs without improving this testable uncertainty.
Integer scale-one arithmetic avoids fractional rounding choices; f64 and fixed
point remain future options. Artifact ingestion, governance, serialization and
storage belong to their existing authorities. See the foundation document for
precise reconnaissance, execution evidence, limitations and next experiments.
