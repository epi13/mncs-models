# RFC 0004 — Residual decisions and proportional native execution

Status: implemented experimental native slice, extending RFCs 0002 and 0003.

## Motivation

The earlier synthetic experiments verified mechanics. Informed deterministic rules
won both benchmarks; an isolated composition edit regressed held-out accuracy.
They established neither operational utility nor LLM authoring efficiency. Preserve
that evidence and make deterministic resolution the first path, not a competitor
that a model is invoked automatically to replace.

## Residual contract

A Boundary names an event, unresolved question, established-evidence reference,
decision time, and an externally supplied deterministic resolution. ResidualSpec
pins a specific model/revision, feature contract, benefit justification, expected
avoidable agent milliseconds, numerical operation/parameter budgets and abstention
margin. Features carry source references, independent view identities, availability
times and refusal statuses. These are evidence-owner assertions, not authenticity
or permission decisions made by models.

`gate_residual` takes no Model. An established answer bypasses model loading,
validation and arithmetic. An unresolved case is eligible only for its named
question, justified expected benefit and available pre-decision evidence.
`decide_residual` recomputes this gate and validates the exact supplied model;
it does not accept a caller-forged eligibility/admission flag. Results distinguish
established answers, candidate predictions and fallback, with missing evidence,
contradiction, future evidence, invalid contracts, resource refusal and abstention
as explicit reasons. A prediction never becomes an execution permission.

VerifiedOutcome is separate from Features and discriminates observed evidence from
heuristics and predictions. Native accounting reports both residual-case coverage,
errors/abstention and end-to-end established/residual outcomes. It rejects mismatched
or pre-decision outcome references and prediction-as-outcome tags. Authentication,
independent custody and the truth of source metadata remain with existing authorities.
UtilityComparison compares a common operational cohort in separate units; it does
not add VM steps to agent milliseconds or authorize deployment. Mechanical fixtures
cannot establish operational improvement through this comparison.

## One numerical representation, smaller native backing

Parameters.values becomes an immutable `[i64; up_to 100]` view in the existing Model.
There is no second model type or numerical runtime. Validation checks sufficient
length, active parameter bounds, zero padding and unchanged identity/lineage rules.
Explicit 5-, 20- and 100-slot materializations support immutable updates without
`replace` on a view. The generic exact-array rebuild shares the copying operation;
exact-to-view borrows are explicitly typed where required by the current frontend.
`compact` creates fresh backing at the smallest bucket; it never merely slices a
large allocation. `edit` validates, rebuilds and revalidates. Invalid padding cannot
be discarded to make an invalid model appear valid. Existing supplied 100-slot
parameters remain accepted and count as 100 slots, not magically compact storage.

Compaction preserves numerical semantics and revision references; serialized bytes
change and require a fresh content/artifact identity from the owning compiler/Store
contracts. No private digest or registry is introduced. Empty DAG rows carry no parameter
backing; a new small assembly does not inherit unused 100-slot dummy arrays. The view capacity is not
the physical allocation length; source materialization and runtime live length
establish the logical payload accounting. Peak VM arena/stack/RSS is not inferred
from logical bytes, and arbitrary borrowed short views may retain larger backing.

## Admission and repeated execution

The one numerical kernel now traverses active input/output lanes. Safe entrypoints
validate the exact immutable model. Full graph admission already validates component
parameters, so it does not immediately scan them again during the same invocation.
`run_projected` validates the requested dependency slice and global identity clashes,
not unrelated model parameters. Its Run declares `admission_scope = 1`; ordinary
`run` declares full admission scope 0. Projection is not certification that the rest
of the graph is valid. Connection bounds are checked before reverse dependency
marking; invalid required nodes reject. All original refusal/provenance paths remain.

Lexical four-item model and graph batches reuse admission only while the same exact
immutable value remains in the validated call chain. Changed weights, graph inputs
or revisions enter fresh admission. There is no persisted `validated=true` field,
unchecked digest equality, cached caller certificate, registry or model service.
Mathematical helper functions have documented preconditions, like the prior layer
helpers; they are not safe untrusted entrypoints or admission authorities. Current
MNCS lacks opaque/private generic record contracts for an unforgeable reusable
artifact across arbitrary calls. Such reuse remains unimplemented. Each independent
native call revalidates; the existing runtime enforces its separate step budget.

## Experimental boundary and ownership

TrialPlan checks bounded, disjoint event-group partitions, evidence references,
parameter and edit budgets. Submission pins an artifact/author and freeze time;
review checks freeze-before-open chronology. Cost fields preserve unknown token/time
measurements. Pure native bookkeeping cannot prove secret custody, authenticate
artifacts, or guarantee that an author did not inspect a held-out answer. External
owner-controlled datasets and a separate author/reviewer boundary are prerequisites
for a controlled LLM trial. Numeric JSON invocation demonstrates data interchange,
not LLM authoring efficiency. mncs-learn retains update governance and optimization;
its inspected native operators are centroid/no-learning, not a neural optimizer.

A bounded read-only operational audit found no suitable receipt-aligned labeled
cohort in the selected Forge context. No new synthetic benchmark substitutes for
utility evidence. See OPERATIONAL_EVIDENCE.md for the candidate, sources and precise
missing data. No Forge, Doctor, Fabric, Environment or learning policy is modified.

## Verification and compatibility

Preserve the thirty native tests and their historical findings. Parameter-field
construction moves through explicit views, and the resource expectations change
where duplicate admission scans are removed. Shared mechanical constructors are
factored into one fixture module; test names and benchmark answers are preserved.
Additional tests cover compact buckets, atomic edits, lexical admission reuse,
projected scope, residual gating, chronology, outcome typing, split integrity and
separate-unit usefulness accounting. Native callable probes separate construction,
validation, cold execution, batch reuse, revision and revalidation. Host scripts
transport typed values and hash artifacts; they perform no inference or fitting.
Historical execution receipts are retained under outputs/history/a5c0b44.

## Subsequent extension

RFC 0005 adds referenced demand review and bounded permitted-operation selection
without changing this binary residual gate or the canonical numerical runtime.
Its audit preserves the negative utility findings and does not promote a learned
guide or operational integration.

## Complete-outcome test replay

The trial module now also supports `TestReplayOutcome` and
`evaluate_initial_test`, using the existing RFC 0005 `GuidanceProblem`. This is a
retrospective evaluation contract, not a new learned selector. It requires every
permitted candidate's observed native assertion verdict and measured cost against
one frozen source/dependency/toolchain/inventory reference. Exact candidate,
event, question, state, permitted-set and time joins are checked. Predictions,
Unknown verdicts/costs, duplicates, missing alternatives, unavailable or over-budget
candidates and mixed units refuse. A per-row cost limit of 10^12 and the eight-row
bound keep unsigned sums safe. No saturation or inferred alternative is used.

The chosen operation may be zero for abstention; that row stays accepted in the
evaluation denominator when the outcome matrix is complete. An all-pass source
has no failure-discovery opportunity: `oracle_cost_known=false`, rather than a
fabricated zero latency. A discovered assertion failure can have a zero measured
cost, so the flag is authoritative for numeric interpretation. The retrospective
cheapest-failing cost is an oracle lower bound, never a pre-decision feature. Full
mandatory executions and measured total cost remain reported for every choice.
The existing baseline path/operation is retained, including ties and established
bypass; the replay neither resolves those ties nor certifies residual eligibility.

These pure records validate joins, not source authenticity, independent custody,
rights or actual outcome truth. External owners must bind references to exact
artifacts and preserve source/chronology. VM-cost sums are not additive CLI wall
latencies or causal work savings. The first source-bound replay and its rejected
learning cohort are recorded in `docs/TEST_PRIORITY_EVIDENCE.md`. Prior native
model, composition, direct-weight and negative utility contracts are unchanged.
