# RFC 0003 — Bounded native micro-model composition

Status: implemented experimental DAG subset of RFC 0001, extending RFC 0002.

## Motivation and decision

A useful local prediction need not absorb its consumers or their parameters.
Represent an assembly as a bounded, topologically ordered table of independently
identified nodes and explicit lane connections. Reuse Model, Parameters, edit and
infer from micro.mncs; do not flatten the parameter state or create a graph-specific
numerical runtime. All authoritative execution and evaluation remain MNCS.

The first envelope is sixteen nodes and eight input/output lanes per node.
Connections refer to external lanes or outputs of strictly earlier rows. This
makes cycles, self-loops and forward references invalid without an unbounded
scheduler. The bound is a deliberate implementation scope, not a claim that the
language cannot represent fifty nodes. A ten-node connected sensor composition
exercises the same execution mechanism as the two/three-node examples.

## Primitive contracts

Node purpose: an addressable local model or deterministic combination. Its identity,
input links, input width, operation, output contract and optional abstention margin
are explicit. Learned nodes retain a complete independently revisioned Model.
Sum adds scalar inputs into one output; Concat preserves input order in a vector.
Learned glue is an ordinary learned node, not a separate ontology.

Link purpose: route one numeric lane. Source zero means an external observation;
1..16 means a prior table row. Lanes and dimensions must be compatible. A nonzero
opaque semantic contract reference must match its source declaration. Native
records, enums and Signal provide representation types; reference matching adds
semantic interface checks without a second type language or registry. All lanes of
one output share its declared contract in this subset. Hidden embeddings and
representation alignment are not inferred.

Assembly purpose: preserve topology, independent component boundaries and an
identity/revision/parent/provenance reference. Model revision changes do not rewrite
other model parameters. rebind validates the supplied model, identity and topology,
requires a new assembly revision, and returns an immutable candidate or the original
on refusal. An older valid component may be rebound for rollback under a newer
assembly revision. Reusing a parameter revision with different numerical values
is rejected. Handles are caller-owned references, not content digests or authority.
Source and executable artifacts are bound by existing compiler identities and the
verification transport's SHA-256 receipts; persistence/rights remain external.

Execution purpose: evaluate one requested output and its transitive dependencies.
Reverse dependency marking and a forward pass provide bounded reuse and fan-out.
Independent nodes have parallel semantics: either legal ordering gives the same
result; the current executor runs serially and does not claim actual concurrency.
The full assembly is validated even for a subset request. Per-node traces preserve
model identity, parameter revision/provenance, output status, contributing ancestor
bits and external-evidence lane bits. The run binds assembly identity/revision,
source event and evidence references. No model receives a failed upstream output
as numeric zero. Input states are supplied by evidence owners, not authenticated
by a model. A single Observation must already align its lanes to one event.

Numeric contracts: reuse bounded scale-one i64 inference; each incoming lane must
be within -1000..1000. Larger intermediate outputs remain inspectable but are
refused at a downstream numeric interface. Sum is bounded by eight such lanes.
No automatic clipping, quantization, rescaling or hidden adapters are introduced.
Margins apply only to scalar outputs; abstention returns no numeric output.

Failure contracts: invalid graph/component, unavailable evidence, contradiction,
abstention, exhausted node/MAC budget and numeric-interface refusal are distinct.
No prediction gains permission, policy authority, recovery execution or verified
outcome status. Deterministic consumers can bypass the whole assembly.

## Resource and implementation obligations

Count active parameters, fixed allocated parameter payload, connection capacity,
intermediate lane storage, validation slots, executed nodes, and active mathematical
operations. Native VM steps and compilation-plus-suite time supplement these
logical counters. They do not establish ABI size, peak process memory, cycles,
energy, agent token savings or production benefit.

Retain the canonical 100-slot parameter array for now. A native bounded-view
functional-update probe is refused with MNE198; replacing the model implementation
with a host allocator is not justified. The measured overhead is a result to
address through native general facilities, not hide behind nominal parameter counts.

## Verification and integration impact

Preserve the fourteen RFC 0002 tests. Add native witnesses for sequential, parallel,
deterministic and learned composition, invalid contracts/dimensions/cycles,
revision/rollback, unavailable/contradictory/abstaining inputs, budgets, numerical
bounds, ten-node execution and a subset request. Freeze a separate synthetic
held-out fixture and compare local, composed, deterministic and standalone methods.
Keep unsuccessful tuning results. Test output and native callable measurements are
source-bound; no host graph runtime or model evaluator is permitted.

Only mncs-models changes. No operational integration or external consumer migration
is required. Recurrence, routing, dynamic discovery, storage, governed learning,
LLM APIs, distributed scheduling, authenticated lineage and deployment remain
outside this executable subset. See docs/COMPOSITION.md for results and limits.
