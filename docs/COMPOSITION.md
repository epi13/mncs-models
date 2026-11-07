# Native compositional micro-models

Historical phase record: [RFC 0004 and current residual execution](RESIDUAL_INTELLIGENCE.md) extend the parameter representation and admission paths described here. Historical benchmark findings and exact receipts are preserved under `outputs/history/a5c0b44/`.

The executable contract is [RFC 0003](../rfcs/0003-native-composition.md).
`src/models/compose.mncs` extends the canonical `Model`/`infer` implementation;
it is not another model runtime. The broader graph charter still exceeds what
this bounded acyclic subset implements. The previous five-parameter experiment
and its stronger deterministic result remain unchanged and verified.

## Construct, inspect and revise

Run `python3 scripts/verify.py` from this repository. `--suite foundation` preserves
the original fourteen tests; `--suite composition` runs the composition suite and
native callable measurements. MNCS Language and Test are resolved through the Git
common directory, including from nested linked worktrees. Explicit environment
variables retain the prior toolchain selection behavior. Application artifacts use the native tool's bounded shared cache in the Git common
directory, separated by compiler executable path; an explicit cache override wins.
Python only invokes the
native compiler/Test path and packages hashes and observations; it performs no
inference, routing, labeling, evaluation or parameter optimization.

The constructors in `tests/native/composition.mncs` are executable examples:

1. Construct independent Models with supplied Parameters, and verify their local
   behavior using infer or a single-node target request.
2. Put each Model into a learned Node with the same identity. Declare each input
   as a Link, output contract reference, and optional scalar margin (-1 disables).
3. Build an Assembly with a topologically ordered node table, active count,
   external lane contracts, identity/revision and provenance reference. Initialize
   unused rows with empty_nodes and unused links with blank_link.
4. Call assembly_valid, then run with an Observation, 1-based target row and Budget.
   Inspect each Trace, its output/status, model revision/provenance, ancestor bits
   and external source mask. Inspect Assembly to recover precise input connections. `component_row` resolves
   a stable component identity to its current row; connection rows remain explicit.
5. Call the existing edit on one node's Model. Rebind that candidate with a new
   assembly revision and provenance. Other models' parameters are retained exactly.
6. Rerun local and whole-assembly regression; rebind the previous Model under a
   newer assembly revision to roll back a failed candidate.

Topology belongs to Assembly/Node/Link; parameter values remain in independent
Model records. Changing one weight does not reconstruct every other parameter
vector or recompile inference. Immutable aggregate values may be physically copied
by a backend; a small semantic intervention is not a zero-copy guarantee. Model
and artifact handles remain opaque references to existing identity authorities,
not an internal registration service or authenticated content identity.

## Execution and refusal

A Link names a source row and lane plus the semantic contract it expects. Row zero
means external input. Every component source must be strictly earlier than its
consumer. Shape, lane, semantic reference, model identity, dimensions, parameter
bounds and active-link padding are checked before execution. Numeric values use
the native Signal type; the semantic reference is not a new type description
language. The initial contract treats all output lanes of a node as one semantic
kind. Connect meaningful scalar predictions initially; it does not align unrelated
hidden embeddings automatically.

Independent branches do not read each other and can be legally reordered, with
links rewired if necessary. This is parallel semantics, not simultaneous execution:
the current executor is serial. Sum and Concat are explicit deterministic nodes;
learned glue uses the same Model/infer operation as local specialists. Fan-out
reuses an upstream trace, and fan-in is explicit ordered input lanes.

One requested output executes only its ancestors after validating the whole table.
Unneeded nodes retain empty traces. Full-assembly validation costs remain even for
a single requested leaf; no unvalidated cached admission token is introduced.
Incoming links must remain in -1000..1000. A larger valid local output can be
inspected, but consuming it downstream produces a numerical-interface refusal.
No implicit rescaling or saturation occurs. Inspection/resource helpers assume
an admitted assembly; run and rebind validate their untrusted assembly inputs.

Run/Trace status codes are: 0 valid, 1 unavailable, 2 contradiction, 3 invalid,
4 abstention, 5 budget refusal, 6 numerical-interface refusal. Failed outputs have
zero width; they never enter downstream inference as numeric zeros. Missing
source references refuse, and external status flags propagate. All external lanes
must already refer to the run's single event; semantic conflict detection and
authentication remain with source authorities. Scores are uncalibrated quantities.
The source evidence references, model revisions and provenance references are
retained in the run and traces. These are lineage references, not rights checks.

## Frozen synthetic experiment

The held-out fixture is `tests/fixtures/composition_cases.mncs`, SHA-256
`4a57eef685758e2d2b29c1eb468ef4c5fae593feaccb3ccf878f8b8903a24437`.
It was frozen before the first benchmark execution and was not used for tuning.
It has 32 unique event groups 101..132 with signature severity, repetition,
pressure and unhealthy signal. They are synthetic, not operational traces.
A declared simulator labels additional diagnosis useful when severity and pressure
are both at least 2, or repetition is at least 3 and unhealthy signal at least 2.
Labels do not come from any tested model. The strong deterministic baseline knows
this rule. Thus the benchmark can measure mechanics, regressions and representational
cost, but cannot establish real operational prediction value or generalization.

Construction and tuning examples are statically separate from `held_out()`.
The two tuning examples are `(2,0,2,0)` positive and `(0,0,0,0)` negative.
Case numbers 1..4 and 51..52 in source comments are documentary phase labels;
the generic unit-test observation constructor uses placeholder event 900. The
held-out runner instead binds each fixture event 101..132 and distinct per-event
evidence references. These are synthetic group identities, not real trace IDs.
Each specialist computes `relu(2*severity + repetition - 3)` on its own two inputs,
with the environmental specialist receiving pressure/unhealthy instead. Each has
three active parameters. Initial learned glue computes `A+B-3` with three more.
The local tuning edit changes only the glue bias from -3 to -1. Classification
uses score > 0; margins are disabled for these benchmark scores.

| Method | Correct / 32 |
| --- | ---: |
| Diagnostic specialist alone | 21 |
| Environmental specialist alone | 22 |
| Initial learned composition, 9 parameters | 25 |
| Edited learned composition, 9 parameters | 20 |
| Deterministic sum + threshold 3 / threshold 1 | 25 / 20 |
| Equivalent initial / edited standalone, 13 parameters | 25 / 20 |
| Standalone linear estimator, 5 parameters | 24 |
| Strong deterministic simulator rule | 32 |

The tuning edit repairs its local positive example and preserves its negative
example but harms held-out performance. Reject that edit and restore the original
component. No further weights were chosen from these held-out results. The native
snapshot test freezes the observed counts; it is regression evidence, not new
training evidence. Standalone equality is also checked: its two hidden neurons
encode the same local functions, with explicit zero cross-connections. Deterministic
glue can reproduce either learned scalar combination exactly. Learned glue provides
no demonstrated benefit here. The initial composition beats either individual
specialist, but both deterministic computation and the small standalone alternative
remain serious competitors. No conventional optimizer or LLM API was introduced;
learning governance remains with mncs-learn.

This does not establish the hypothesis that LLM construction is more efficient.
One isolated parameter edit out of nine demonstrates addressability and limited
regression scope, not agent token/time savings. The equivalent standalone can
make the same correction at slot 12, so this benchmark does not demonstrate a
smaller intervention than that standalone model. No matched monolithic LLM-authoring
trial, training baseline, calibration or independent evaluation was performed.

## Scale and proportional cost

The same executor runs a ten-node sensor example: eight independently identified
one-input rectified local severity models, one learned four-way aggregation, and
one learned five-way aggregation including the earlier aggregate. These are real
connections and distinct models, not repeated unconnected invocations. Local inputs
come from eight distinct sensor lanes. It is a scale/mechanics witness, not another
predictive-performance claim.

| Property | Three learned nodes | Ten learned nodes | One leaf requested in ten-node assembly |
| --- | ---: | ---: | ---: |
| Active parameters in assembly | 9 | 27 | 27 |
| Executed nodes | 3 | 10 | 1 |
| Active multiplies / additions | 6 / 6 | 17 / 17 | 1 / 1 |
| Parameter slots checked, validation + inference | 600 | 2000 | 1100 |
| Allocated fixed parameter payload | 12,800 bytes | 12,800 bytes | 12,800 bytes |
| Live connections | 6 | 17 | 17 |

The table's parameter payload includes all sixteen allocated Node slots, including
unused and deterministic rows. Each embeds the canonical 800-byte parameter array.
It excludes metadata, ABI padding and runtime copies. Active payloads are only
72 and 216 bytes: the gap is material. Connections occupy sixteen times eight
three-u64 Link slots, or 3,072 logical bytes. Traces reserve sixteen eight-lane
signals (1,024 lane bytes), plus widths, statuses, identities, source masks and
lineage references. The needed-node mask occupies sixteen logical booleans.
Each Node also contains its model's topology, identity/revision/provenance,
operation, width, output contract, margin and eight links. Assembly has external
contracts and revision metadata; Run retains source references and the full traces.
These complete structures are bounded, but their peak backend memory is unmeasured.

Validation traverses sixteen rows, checks eight link slots per live node, and scans
sixteen identity candidates per live node, in addition to model validation. Reverse
dependency closure traverses sixteen rows and eight slots per needed node. Execution
scans sixteen rows and eight input slots per requested node, plus the existing
padded micro inference loops. `connection_checks` reports reserved link-check slots
(validation plus requested gathers), an upper bound when failure ends a gather.
`parameter_checks` counts the model validation slots for admitted valid assemblies.
These are not VM instruction counts. Node/MAC budgets bound model execution, not
compilation, validation, dependency discovery, total VM steps, or peak memory.
The native caller's independent step budget bounds the whole execution.

Native callable measurements and compiler-owned test output under
`outputs/composition/` record actual VM steps and suite wall time. The five cost
probes include construction, validation and execution for their named method;
they are not isolated inference latency. The standalone probe uses the equivalent
initial function. The deterministic probe includes the same observation constructor.
Final native probe observations:

| Probe (construction + validation + execution) | VM steps | Returned value |
| --- | ---: | ---: |
| Three-node initial composition | 18,004 | 3 |
| Equivalent standalone | 2,747 | 3 |
| Strong deterministic classification | 54 | 1 |
| Ten-node sensor assembly | 65,335 | 16 |
| One requested sensor leaf in that assembly | 41,415 | 2 |

Source file bytes, executable identity and native returned values are recorded.
Compilation/receipt wall time does not estimate environmental benefit.

The bounded-view probe demonstrates that native views can represent smaller read
windows, but functional `replace` on a view is refused with MNE198. Retaining exact
arrays keeps one editable canonical representation. A private allocator or second
compact inference runtime would obscure the tradeoff. A future native parameter
representation must preserve immutable edits and artifact identity and measure
actual retained backing storage, not merely claim a smaller logical view length.

Fifty nodes were not implemented or measured. Sixteen is this phase's chosen bound,
not a discovered compiler maximum. Increasing it requires changing bounded table
and provenance-mask capacities and remeasuring the same algorithm; it does not
require a new model or graph ontology. The fixed storage and repeated validation
already justify investigating smaller native records/parameter updates before
raising the bound. No arbitrary recurrence, scheduling, dynamic discovery or AutoML
was added to reach a component-count target.

## Environment and delivery

Authoritative main started at bcf17bd; no subsequent remote changes were observed
at entry. The original untracked graph experiments were inspected and preserved.
They are not an alternate canonical runtime. Current heads inspected: Language
f8212ed, Compiler f372a6e, Test d51958b, Stdlib 7f1d3ba, Commons c53ae0b and
Learn 24f4d25. Actual execution is bound to the compiler binary hash and native
artifact identities, not an assumption that a checkout head attests a binary build.
The existing native Test entrypoint and library resolution are used.

Environment entry granted this isolated workspace write scope, but claim admission
still required the primary checkout's repository manifest. The primary checkout
predates that manifest on its historical branch. The exact already-committed main
manifest was temporarily materialized using exclusive file creation, without
modifying any foreign file, to satisfy Environment's ordinary repository-identity
check. Environment then acquired the exact linked-worktree claim
`claim:mncs-models:worktree:e70550c8a6eb` in session `ses_54649d7cd1dac21d`.
No Environment code or registration checks were bypassed or modified. That claim
is released and the temporary primary-checkout registration file removed during
delivery cleanup. The foreign branch, untracked files and source work remain intact.

## Next bounded work

Prefer the simulator's deterministic rule here. For a real uncertainty, obtain
read-only authorized event-aligned traces and freeze a new split before construction.
Measure complete benefit, invocation/validation overhead, false diagnostic actions,
and maintenance burden. Test compact editable parameter storage through the owning
language/stdlib facilities, then reassess node capacity. A matched component versus
monolithic authoring trial should measure agent intervention separately from model
accuracy. Keep model promotion/rejection with mncs-learn and existing authorities;
no operational tool integration is part of this phase.
