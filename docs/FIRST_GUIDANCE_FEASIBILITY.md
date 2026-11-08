# First executed direct-weight guidance experiment

A five-parameter native affine model was authored from six development source
states, executed, revised through two canonical parameter edits, and evaluated on
six further controlled source states. The revised model selected a failing test
first in 3 of 5 failure-bearing evaluation groups; the initial model reached 2/5.
A competent deterministic rule using the same information also reached 3/5.
For these inexpensive probes, selection and feature preparation cost more native
VM work than simply executing the tests. Prefer direct verification here.

This establishes narrow, executed feasibility. It does not establish natural
operational usefulness, causal agent savings, independent held-out generalization,
or an advantage for learning over the informed rule. No live tool uses the model.
The complete results and measurements are in
[`outputs/first-guidance`](../outputs/first-guidance/README.md).

## Decision and independent outcomes

The question is which of three permitted regression probes should run first after
an isolated change to the same small calculation. The specification is
`min(12, max(0, amount-credit) + (urgent ? 3 : 0))`. The fixed probes are
`(8,2,false) -> 6`, `(2,5,true) -> 3`, and `(14,1,true) -> 12`.
All three remain mandatory; prioritization can affect early failure discovery,
never final verification coverage or authorization.

`experiments/first_guidance/s01.mncs` through `s12.mncs` are separate immutable
implementation modules. They contain concrete source changes, including arithmetic,
predicate, selected-value and new-control-flow changes, plus benign changes.
They are compiled together for economy, but each probe calls only its own pure
variant. Groups are module/source states, not repeated test rows or independent
operational commits. The native Test runner produced the actual assertion results;
no simulator or model assigned failure labels. The specification and probes were
fixed before weights or predictions existed.

The pilot immediately demonstrated different outcomes: s01 failed probe 1 while
s02 failed probe 2. Development eventually contained six failed and twelve passed
assertions; evaluation contained five failed and thirteen passed assertions.
All-pass states remain in the evidence. The earlier all-pass campaign and its
negative findings remain unchanged; this study does not relabel them.

## Information and baselines

The shared pointwise scorer receives four scale-one integer lanes:

1. Reference value-flow activation of the changed source arm.
2. Whether the relevant reference predicate selected its arm.
3. Number of observed downstream clamps after that source region.
4. Earlier development-state failure count for that probe.

A native clean-reference projection computes the predicate/clamp observations.
The source owner supplies a fixed `Region` enum from the source change. This is a
small explicit fixture annotation, not an automatic LSP or compiler-impact claim.
`select` evaluates eagerly, so these are selected-value-flow facts, not CPU line
coverage. No mutant identity, test name, future verdict or future measured cost is
a model input. Earlier Test verdicts supply history; final counts are frozen at
`[2,3,1]` before evaluation. Source tags are legitimate structural information,
shared with every baseline, rather than defect-class labels.

All policies use the same readiness, identities, pre-decision data and prior clean
reference costs. The deterministic comparisons are: activation then least cost;
activation then historical failures/cost; and an informed lexicographic policy
preferring the selected predicate, fewer downstream clamps, then history/cost.
The informed policy is the strongest tested same-information baseline. Ties remain
explicit abstentions. A unique affected arm bypasses neural inference; unsupported
new control flow refuses model use. The cost/history policies can still use their
known inputs when the richer context contract is unsupported.

These rules do not prove which assertion will fail: a changed threshold can
invalidate reference-path intuition. That uncertainty remains after identity,
authority, dependency and readiness checks. Exact output execution is the
independent outcome operation itself, rather than a cheap pre-decision label.

## Authored parameters and source chronology

The model is the canonical `mncs.models.micro.Model`: four inputs, no hidden layer,
one output, identity activation, five i64 parameters, 40 logical active payload
bytes. Scores are uncalibrated rankings, not probabilities. Five is a declared budget,
not a proven minimum: activation also gates eligible probes, and a common bias
does not change ranking. A parameter-reduction experiment was not performed.

| Revision | Parent | Weights: activation, selected predicate, clamps, history, bias | Provenance |
| --- | --- | --- | --- |
| 1 | 0 | `[3,0,0,1,0]` | 9401 |
| 2 | 1 | `[3,2,0,1,0]` | 9402 |
| 3 | 2 | `[3,2,-3,1,0]` | 9403 |

Model identity is 9301. The agent explicitly chose these numerical values from
permitted development evidence. Revision 1 uses activation/history. The two planned
`micro.edit` calls add reference-predicate support and penalize downstream masking.
Both native edits succeeded. They are actual numerical authorship and edits, not
an optimizer relabeled as authorship or reused historical fixture vectors.
The first native call abstained on development s03 with scores `[4,4,3]`; the
revised model distinguishes that cap probe. Every initial, intermediate and revised
artifact and native output is retained. There were zero weight edits after final
outcomes were executed.

Development is exploratory. The first two pilot feature rows were reconstructed
from the immutable reference after pilot outcomes existed; they are not claimed
as historical pre-decision captures. An initial transport projection was moved to
native code before final evaluation, with exact equality of all development
feature values checked. The author constructed/could inspect all controlled source
variants. There was no separate blinded custodian. `freeze.json` pins features,
models, methods, source and compiler before **final execution**, and the native
predictions were recorded before that Test invocation. This is not sealed held-out
custody. The same frozen predictions were reproduced by native outcome evaluation.

## Comparative result and retained failures

| Method | First failure selected / 5 opportunities | Bypass groups | Abstentions / all 6 groups |
| --- | ---: | ---: | ---: |
| Activation + prior cost | 1 | 1 | 5 |
| Activation + history/cost | 2 | 1 | 0 |
| Informed deterministic rule | 3 | 1 | 1 |
| Initial five-parameter model | 2 | 1 | 1 |
| Revised five-parameter model | 3 | 1 | 2 |

Unsupported s11 is included as a missed opportunity, not excluded. The unique
cap-arm s09 is a deterministic bypass and is not credited to neural inference.
Among the three supported, unresolved, failure-bearing groups (s07, s08, s10), the
initial model selected a failure in 1/3 and the revised model/informed rule in 2/3.
The remaining all-pass group has no failure-discovery oracle cost; it is not
assigned an invented zero failure latency or counted as a correct classifier label.

The revised model and informed rule both miss s10: changing the floor threshold
makes a previously unselected probe fail. Revision 3 abstains on unsupported s11
and ties on all-pass s12. No repair was made after these results.

A descriptive post-evaluation ablation zeroed the two context lanes while retaining
revision 3's fixed weights. Native inference reproduced all six initial-model
choices. This ablation is not a new untouched evaluation. Both models use five
parameters, so increased capacity did not explain the improvement. In development
s01, all limited vectors are identical `[1,0,0,0]`, but their assertion verdicts
differ. A larger shared pointwise scorer with the same limited inputs cannot
separate those rows; adding identities or positional information would change the
information contract. No larger-model or optimizer superiority claim is made.

## First-class components and ownership

The implemented pathway is a native source/reference projection, ordinary typed
`Model` values, canonical `infer`/`edit`, deterministic bounded selection and the
existing native complete-outcome evaluator. Test independently executes all probes.
The model is a computational component inside that pathway, not an authority above
it. One shared model revision scores candidates; the two evaluated revisions are
alternatives, not a specialist ensemble. A graph or extra neural primitive was
unnecessary. The canonical numerical/composition/gating implementation is unchanged.

RAVEL currently advertises experimental adaptive-evidence-strategy and
verification-obligation-plan contracts. Its native obligation planner joins
compiler-owned impact, obligations, test declarations and fresh/noncontradictory
evidence; its task context refuses stale, unauthorized or over-budget requests.
Those responsibilities remain there. All three study probes concern the same
function and remain required, so a RAVEL obligation plan could supply the permitted
inventory while a guide ranks within it. No RAVEL ranking output was consumed or
benchmarked in this experiment, and no parallel retrieval or impact implementation
was built. Native `mncs-learn` currently implements centroid/no-learning operators,
not a dense-weight optimizer. This study makes no learning-governance, promotion,
optimizer comparison or LLM-efficiency superiority claim.

A live consumer would still need owner-authenticated artifacts, demonstrated
reliability/support bounds, resource justification, current RAVEL/Environment
context and fresh execution admission. The native opaque handles and joins do not
create any of those rights or proofs. Mandatory verification remains independent.

The project Environment definition was also corrected: its lasting goal is now
native Models development/research, rather than one test-priority campaign, and
experiment-specific disabling of verification/actions/diagnostics/family passes
was removed. Writable scope remains Models only. No operational provider capability
was invented; entry still reports its actual available bindings.
