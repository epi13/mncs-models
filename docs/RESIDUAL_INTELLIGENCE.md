# Residual intelligence and proportional execution

The implementation contract is [RFC 0004](../rfcs/0004-residual-and-proportional-execution.md).
Model structure, inference and evaluation are native MNCS. There is one Model,
one numerical kernel, and the existing DAG. No operational decision-making tool
was integrated and no learning-governance or model-storage service was added.

## Confront the prior findings

The five-parameter synthetic fixture reached 7/8 after modification, while the
informed deterministic rule reached 8/8. The composition fixture reached 25/32;
a local edit reduced it to 20/32. Equivalent standalone networks matched it,
and the informed deterministic rule reached 32/32. These remain mechanical and
regression findings, not operational utility or LLM authoring-efficiency evidence.
Exact previous receipts are preserved under `outputs/history/a5c0b44/`; the commits
bcf17bd and a5c0b44 retain their sources. Current tests preserve all thirty cases
and numerical outcomes. Resource assertions change where duplicate validation
has actually been removed. The eight/32-case fixtures are not tuned again here.

## Separate deterministic resolution from a residual question

`src/models/residual.mncs` distinguishes:

- Boundary: an event, specific question, authoritative established-evidence reference,
  decision timestamp, and externally established deterministic resolution.
- ResidualSpec: one intended question/model/revision and feature contract, a benefit
  justification reference and expected avoidable agent milliseconds, operation and
  parameter limits, and scalar abstention margin.
- Features: independently referenced views, event identity, availability timestamps,
  status flags and numeric input lanes.
- ResidualDecision: established answer, candidate prediction, or fallback with an
  explicit reason. Predictions retain the model/revision and input references.
- VerifiedOutcome: independently supplied observed evidence, distinct from heuristic
  or prediction tags. It is never a model feature in this contract.

First call `gate_residual(spec, boundary, features)`. It takes no Model. Known
resolutions return immediately without model loading, parameter validation or
neural arithmetic. Eligibility is tied to a named unresolved question, justified
expected benefit and evidence available by decision time. Expected milliseconds
are a hypothesis from the owner, not measured savings or a probability.

Only an eligible case should load/construct its model and call `decide_residual`.
That function recomputes eligibility; it never trusts a caller-supplied gate flag.
It validates actual parameters and the intended model/revision, enforces numeric
operation/parameter budgets, and preserves abstention. An invalid model or mismatch
cannot displace an established deterministic answer. VM time/step enforcement
remains with the actual native runtime; MAC counts do not enforce a VM budget.

Reason codes: 1 unjustified/mismatched residual question, 2 unavailable evidence,
3 contradiction, 4 evidence available only after the decision, 5 invalid model or
contract, 6 numerical resource envelope, 7 abstention. Scores are not calibrated
probabilities. Feature status 0 is usable, 2 contradictory, other nonzero statuses
unavailable to this predictor. Normal fallback and agent-assisted diagnosis remain
valid paths. A model may be retired when a deterministic rule resolves its question.

References and source tags are not authenticated inside this pure library.
Existing owners must establish which evidence is authoritative, align events and
clocks, resolve artifact contents, enforce rights, and verify outcomes. The library
checks bookkeeping/compatibility and chronology, not custody or permissions.
An eligible prediction does not authorize diagnosis, recovery, scheduling or any
other operation. The entire assembly can be bypassed without disabling a baseline.

## Parameter storage and editing

The existing `Parameters.values` field is now `[i64; up_to 100]`. A supplied 100-slot
array still costs 100 logical slots. A five-slot array no longer has to become a
100-slot parameter payload. Existing inference and topology/lineage contracts are
preserved. A model with fewer stored values than its active parameter count rejects;
nonzero inactive padding and out-of-range parameters still reject.

The current language refuses functional `replace` on views (MNE198), but this does
not require a new compiler feature to obtain compact editable models. Native edits
rebuild an exact 5-, 20- or 100-slot array and borrow it as the canonical parameter
view. The common generic exact-array copier performs the update using ordinary
native replace. `compact` materializes the smallest such bucket; it does not merely
slice the original large backing. `edit` validates the old model, rebuilds, records
parent/revision/provenance, and validates the candidate. Refusal returns the original.

For direct construction:

```mncs
let weights: [i64; 5] = [3, 1, 1, 1, -6];
let values: [i64; up_to 100] = weights;
// Use values in the existing Parameters record, and validate the Model.
```

Explicitly typed borrows avoid current frontend coercion limitations on record
fields. `parameter_values` adapts existing exact 100-slot fixtures; arbitrary
native Model records can use appropriately sized typed borrows. Generic record
parameters remain unsupported, so no speculative Model<N> abstraction is introduced.

`compact_assembly` preserves meaningful component identities, numerical state,
connections and semantic revisions. It removes unused/deterministic parameter
backing and compacts active learned nodes. Serialized bytes change, so the owning
Store/compiler must assign a new content identity even though the function and
semantic weight revision are unchanged. No private hash/registry is implemented.

New materialized logical payloads:

| Assembly | Active parameters | Previous reserved payload | Compacted payload |
| --- | ---: | ---: | ---: |
| Three learned nodes | 9 | 12,800 bytes | 120 bytes (15 slots) |
| Ten sensor/aggregation nodes | 27 | 12,800 bytes | 520 bytes (65 slots) |

The canonical empty node now has an empty parameter view. Even without explicit
compaction, the old raw fixture constructors reserve 2,400 bytes for three active
100-slot models and 8,000 for ten, rather than padding all sixteen unused rows.
Directly constructing small models into those empty rows avoids the raw-to-compact
preparation path altogether.

These count logical materialized parameter backing, not peak stack/arena/RSS or ABI
padding. Views and metadata also cost storage. A short arbitrary borrowed view can
retain larger backing; only the compaction constructors guarantee new exact buckets.
Cold compaction temporarily coexists with its input. Sixteen-node metadata, 3,072
logical bytes of connection slots and 1,024 intermediate lane bytes remain; no
allocator or graph redesign hides them. Twenty-slot buckets still overallocate
six-parameter nodes. A standalone model remains preferable when composition has
no measured benefit.

## Admission scope and repeated execution

The native kernel traverses active inputs/outputs. Ordinary `infer` validates the
exact supplied Model on every call. `infer_batch` validates one immutable model
once for four input signals, checking each input separately. It returns independent
success/refusal results; an invalid input never becomes ordinary zero evidence.

Ordinary graph `run` retains full admission, including all active components.
Because that admission already validates their actual parameters, numerical
execution does not immediately scan them again. `run_projected` admits only a
requested dependency slice plus identity clashes and required contracts. Links are
checked before reverse marking, preventing invalid references from reaching unchecked
indexing. The returned `admission_scope` is 1 for projection, 0 for full admission.
Projection can evaluate a valid independent leaf while rejecting invalid required
nodes; it does not declare unrelated nodes valid. Caller metadata and input transport
still carry the bounded graph, so projection is not zero-cost independent loading.

`run_batch` reuses a projected admission for four observations of the same exact
immutable assembly, within one call. Each observation retains its event/evidence
references and per-component traces. A changed model or assembly in a new invocation
is revalidated. Full admission now checks 300 rather than 600 parameter slots on the
raw three-model fixture; a compact three-model invocation checks 15. A projected
leaf in the compact ten-node fixture checks 5 rather than all 65 slots. The original
raw full-graph leaf path remains available and checks all 1,000 slots.

There is no externally reusable `validated=true` certificate. Public mathematical
helpers such as infer_inputs/run_body have validated-input preconditions and are
not untrusted entrypoints or authorities. The language's current public record and
function model does not supply an opaque admission handle. Arbitrary cross-call
admission reuse is deliberately unimplemented; digest or flag assertions would not
safely establish that the executed parameters are those admitted. Existing toolchain
artifact admission and retained runtime sessions remain their owning responsibility.

## Resource evidence

Run `python3 scripts/verify.py` for the 45 native tests and original regression
measurements; run `python3 scripts/measure_residual.py` for stage measurements.
The latter transports native-created Models, Signals and Assemblies into later
native calls, with the compiler ABI checking every nested field. It converts
returned record field tuples to host-input maps and preserves numeric values and
variant names; it performs no model arithmetic or evaluation. Returned values do
not become admission certificates: each independent call validates its argument.
Only lexical native batches amortize validation.

`outputs/residual/stages.json` binds sources, compiler binary, typed argument files,
results, native VM steps and CLI wall time. Stage scopes distinguish construction,
validation, cold inference, four separate validations, lexical batch execution,
revision, revalidation, graph preparation, full/projected admission and residual
gating. VM steps exclude argument decoding/CLI compilation. Wall time includes
cache admission, transport and process startup; it is not inference-only latency.
Pure numerical execution still validates input bounds. There is no unchecked
"warm" timing that quietly discards trust requirements.

Measured VM stages (values transported into the invocation; model construction
is outside validation/inference rows):

| Stage | VM steps |
| --- | ---: |
| Compact five-slot fixture construction | 23 |
| Explicit expansion of that fixture to 100 slots | 1,761 |
| Validate 100 / 5 stored slots | 1,714 / 194 |
| Cold inference, identical weights with 100 / 5 slots | 2,046 / 526 |
| Four independently validated / lexical model inferences | 2,110 / 1,601 |
| One validated five-slot parameter edit / later revalidation | 552 / 194 |
| Three-node preparation and compaction | 15,009 |
| Validate / execute already prepared three-node graph | 2,590 / 6,119 |
| Ten-node preparation and compaction | 56,855 |
| One leaf: full / projected admission on that same compact graph | 10,206 / 2,721 |
| Four projected calls / lexical graph batch | 10,816 / 7,115 |
| Established-resolution gate / eligible-candidate gate | 106 / 425 |
| Eligible residual prediction including fixture context construction | 1,044 |

The 100-slot expansion is an explicit copy probe, not a reconstruction of the old
literal constructor. Do not call its difference from 23 steps a legacy construction
speedup. One-time graph compaction can cost more than an old cold one-shot invocation;
it earns its place only when preparation/storage/reuse benefits justify that cost.
Batch budgets are per observation; the native runtime step budget bounds the whole
batch. Graph rebind still validates untrusted assembly inputs before/after replacement;
its maintenance cost is not measured separately here. Invalid-input partial-validation
costs are not represented by successful-admission counters; use actual VM traces.
Feature references in a decision are supplied context, not a claim that all were used:
`invoked` and `path` distinguish actual learned contributions.

Matched construction + admission + execution regression probes, with the **same
compiler binary hash** as a5c0b44:

| Probe | Historical steps | Current steps |
| --- | ---: | ---: |
| Three-node raw composition | 18,004 | 12,222 |
| Equivalent raw standalone | 2,747 | 2,407 |
| Ten-node raw full invocation | 65,335 | 46,463 |
| One leaf in raw ten-node graph, full admission | 41,415 | 39,470 |

The prior end-to-end graph probe cost 18,004 steps versus 2,747 standalone. Current
same-function probes remain in outputs/composition; historical observations are
retained separately. The new stage probes also expose one-time compaction costs,
so their cost is not hidden inside an apparent steady-state improvement. Compare
matched scopes rather than subtracting unrelated probe totals. CLI admission costs
can dominate wall time for tiny models. Peak memory, power, agent authoring time,
real diagnostics avoided and maintenance savings remain unmeasured.

## Evaluation and usefulness

Native ResidualMetrics separates established cases, residual cases, predictions,
fallback, false positives/negatives and rejected outcomes. `correct_total` is strict
answer correctness at the decision boundary over the supplied full cohort, not a
claim that fallback failed to resolve the eventual workflow. Later agent-assisted
verified resolutions and actual costs belong to the owner observations. Aggregation
expects a nonduplicated cohort; it does not create an event ledger.

Burden/UtilityComparison require the same operational cohort and outcome reference,
record separate construction/maintenance agent time, diagnostics, critical misses,
feature/validation/inference steps and measurement references. Mechanical origin
cannot establish utility. Comparisons remain a vector; no conversion adds steps to
milliseconds or silently amortizes construction costs. These reference checks are
not source authentication, statistical significance, causal attribution, or a
deployment decision. mncs-learn and the existing authorities retain those decisions.

No new predictive-utility benchmark or controlled LLM authoring trial was conducted.
The new fixtures are explicitly mechanical contract tests. The original informed
rules still outperform their models. Read [the operational audit](OPERATIONAL_EVIDENCE.md)
and [the direct-weight trial boundary](DIRECT_WEIGHT_TRIAL.md) for what remains missing.
