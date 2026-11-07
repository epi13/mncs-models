# Native demand and operation guidance

RFC 0005 extends the existing residual boundary to a bounded experimental problem:
which member of an owner-supplied set of permitted deterministic operations should
be considered next? It supplies no permission, invokes no operation and adds no
neural runtime. Environment remains responsible for observation, freshness,
delivery, orchestration and ambience measurements.

## Demand classification

`src/models/demand.mncs` accepts three explicit projections:

1. `AgentDemand`: event/task/state, decision time and observed activity source.
2. `EnvironmentalSupport`: independently sourced capability snapshot, readiness,
   delivery reference/time and number of permitted options.
3. `DemandReview`: retrospective finding, adequacy evidence and exclusion reason.

`DemandEvidence` preserves source reference, authority, event/state join,
availability time and Present/Absent/Contradictory status. Nonzero integer handles
refer into an externally maintained evidence/artifact context, as in the existing
micro-model contracts. They are not identities minted by a registry here. Commons,
Store and rights/provenance retain their shared identity/authentication roles;
production transport must retain full owner references/digests alongside handles.

`classify_demand` implements a conservative projection of reviewed claims. It is
not an automatic detector of equivalent knowledge. A source owner or independent
review must establish the actual claim, sufficiency and the relevant opportunity.
The native function checks structural prerequisites and joins; it cannot establish
truth, authenticated authority, semantic equivalence or independence of references.

| Result | Required reviewed finding and support |
| --- | --- |
| ProvenRedundant | Equivalent sufficient support demonstrably delivered before the decision, ready snapshot, adequacy reference, no exception |
| PotentiallyAvoidable | Relevant ready capability; preservation of outcomes/savings remains unproven |
| ResidualSelection | Multiple legitimate ready options (2–8), explicitly reviewed selection uncertainty |
| MissingDelivery | Reviewed missing deterministic capability or delivery, joined pre-decision capability snapshot |
| LegitimateReasoning | Reviewed novel reasoning; capability availability is irrelevant to that finding |
| Insufficient | Unknown/missing/misaligned/contradictory evidence, timing failure, absent adequacy or an unresolved exclusion |

Activity and support must refer to the decision state. Support must be available
by the decision time. Activity records may arrive afterward; retrospective review
must be available at or after both the decision and activity-record availability. It never becomes a feature for
that earlier decision. Independent verification, changing state, retries after
failure and unknown exclusions prevent a redundancy conclusion. An unsupported
DeliveryGap finding cannot classify an unobserved terminal failure as a defect.
Classifications retain the input/review references and refusal reason. They do
not credit savings, aggregate a burden score, or train a model. Any future cohort
must retain insufficient/excluded rows and a declared sampling/coverage denominator.

## Operation-selection contract

`src/models/guidance.mncs` defines `GuidanceBoundary`, `OperationCandidate`, and
`GuidanceProblem`. The immutable problem declares:

- Exact event, question, state, decision time, established evidence and permitted-set
  reference; one operation contract shared by the candidates.
- Between one and eight uniquely addressed candidates with independent readiness
  and evidence availability. The bounded view has the actual supplied length;
  no eight-element padded allocation or model parameters are required.
- A cost-unit reference, ranking-method reference, maximum candidates and maximum
  individual operation cost. Costs must share the owner's declared unit; they are
  not combined with tokens, VM steps or elapsed time from another source.
- An optional externally established operation. It must belong to the permitted
  set, match its contract, and have joined usable evidence.

`guide_operations` validates the exact supplied problem. It returns:

- **Established bypass**: select the established permitted operation without a
  ranking method, cost estimate, model construction or inference. Unused missing
  candidate observations do not block this projected path.
- **Deterministic suggestion**: choose the unique least declared cost among ready,
  usable candidates within budget. Equal best costs abstain; input ordering cannot
  silently settle a tie. This is a cost baseline, not a usefulness estimator.
- **Fallback**: invalid/duplicate/incompatible declarations, contradiction,
  misaligned or post-decision usable evidence, missing candidates/costs, exceeded
  budget or unresolved tie. No operation ID is returned on refusal.

Unavailable candidates and unknown costs are counted/excluded, never scored as
zero. Contradictory or stale/future usable evidence refuses residual ranking.
All original candidates remain inspectable in the immutable problem. Results
retain permitted/established/ranking/selected-source references, cost unit, counts
and reason. `cost_known=false` on bypass/fallback means the numeric cost field
does not estimate the operation's cost. `candidate_checks` counts admitted rows,
not VM instructions: unique-ID admission also performs n² comparisons, bounded
by 64. A caller may budget fewer than eight candidates, and pays no hidden neural
or sixteen-node graph admission.

The supplied permitted-set reference is an owner assertion binding the exact list,
not authorization authenticated by native record construction. Consumers must
revalidate current permissions/state before execution. Neither a suggestion nor
an established answer can expand that list or grant operational authority. No
consumer is wired to this experimental mechanism.

## Outcomes and future learned adapters

`evaluate_selection` recomputes the selection from the exact problem; it does not
accept an unchecked result token. `SelectionOutcome` refers to the decision record,
actually executed operation, exact event/question/state/permitted snapshot, source
authority, observation time and existing `OutcomeKind`. Prediction/heuristic labels,
pre-decision outcomes and mismatched selections are rejected. Usefulness, work
verification and tool-call measurement each preserve their own Unknown state.
An accepted outcome can still have unknown usefulness or failed verification.
Its tool calls are observed counts, not savings.

External authorities must authenticate the decision record's exact problem and the
outcome, prevent duplicate sampling and enforce outcome independence. These checks
are structural protection against accidental mixing, not a custody protocol.

No learned operation scorer was justified by the inspected evidence. When a genuine
cohort exists, an adapter can use the existing `Model`, `infer`/`infer_batch`, edits,
residual feature checks and composition executor to score the same allowed list.
It must pin model/revision/output meaning, bound total candidate invocations,
preserve unavailable/contradictory inputs and abstention, and earn its cost against
the deterministic baseline. The existing direct-weight partition/freeze protocol
and `mncs-learn` governance remain required. Next-request imitation alone would
not establish useful guidance. Arbitrary planning, live routing, training and
telemetry collection are not implemented here.

## Reproduction and scope

Run `python3 scripts/verify.py`, or `--suite guidance` for the new 26 tests and six
callable probes. `mncs call` accepts the native records through the existing typed
numeric/finite/record/sequence interchange; agents need not edit inference code
to supply a new candidate list. The tests exercise classification prerequisites,
evidence joins, exclusions, permutation/tie behavior, deterministic bypass, unknown
costs, refusal, budgets and observed-outcome separation. The authentic-source audit
is separate from those mechanical fixtures.

Source-bound receipts and complete native-call results live in
`outputs/guidance`. VM steps include fixture construction for the supplied probes;
CLI wall time includes admission/compilation/cache/transport. Neither is agent
reasoning time. Candidate row storage scales with the supplied bound; actual
peak arena/stack/RSS was not measured. Existing 45 tests, model/composition semantics,
prior performance receipts and negative predictive findings remain preserved.

The recorded complete invocations cost 388 VM steps for one candidate, 668 for
two, and 2,992 for eight; established two-candidate bypass costs 529. Classification
costs 360 and incomplete-history refusal 152. See the
[measurement table and representation accounting](../outputs/guidance/README.md).
These measurements include construction and admission, and establish no agent-time
savings or advantage over a model performing a different task.
