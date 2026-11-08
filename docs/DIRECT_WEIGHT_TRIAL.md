# Direct-weight engineering: native mechanism and executed feasibility

The first [executed five-parameter feasibility study](FIRST_GUIDANCE_FEASIBILITY.md)
now records actual LLM-authored weights, native edits, variable Test outcomes and a
negative comparison with an informed rule. It is exploratory, with no sealed
held-out or operational-savings claim. Historical phase findings below remain
preserved; their missing-custody finding does not prohibit exploratory execution.

An agent can supply numerical weights, invoke native inference, use native edit,
inspect outputs and compare revisions without changing inference implementation.
This phase exercises that data interface. It does not establish LLM authoring quality,
edit efficiency, generalization, token savings or operational benefit.

## Native mechanism

`src/models/trial.mncs` provides TrialPlan, disjoint bounded Partition groups,
Submission, AuthorCost, validation and freeze-before-heldout-review chronology.
The plan names a question, construction/tuning/held-out evidence references, a
commitment reference, parameter budget and maximum edit count. Partition groups
must be nonzero, unique and disjoint. Submission records artifact, author and freeze
time; model validity and actual parameter count are checked. Cost flags explicitly
represent unknown tokens/time rather than inventing zero-cost authorship.

This is bookkeeping, not secret custody. Opaque commitment/artifact references must
be resolved and authenticated by existing Store/rights/evidence owners. The native
checks cannot prove that an author lacked the held-out answers, that timestamps
are trustworthy, or that an outcome is independent. Current tooling's public record
values are not unforgeable author/reviewer capabilities. No local claim of a
controlled trial is made from those flags.

## Reproducible numerical interface

Run `python3 scripts/measure_residual.py`. Its authoring argument files supply two
five-element weight arrays and the same four-element feature array to the native
`score_authored` entrypoint. The native artifact is the same for both; only argument
data differ. These are mechanical fixture weights, not an independent LLM trial.
The separate revision_probe uses edit to record revision 2 with parent 1, and the
candidate is revalidated through the native entrypoint.

With the admitted compiler executable, the general interface is:

```bash
mncs call src/models/trial.mncs --module mncs.models.trial \
  --function score_authored --args examples/authoring/initial.args.json --library src
```

The example JSON uses the compiler-owned typed HostExecutionValue ABI. Edit numerical
values in that data file, not the native kernel. For general topologies, use the
existing `micro::infer` entrypoint with a typed Model and Signal argument pair;
`outputs/residual/infer_5.args.json` is a complete compact example. `micro::edit`
accepts Model, parameter index, new numerical value, new revision and provenance.
The fixed five-weight helper is just a convenient caller construction, not another
runtime or the only permitted parameter budget.

## Controlled protocol once suitable evidence exists

1. The task/evidence owner chooses a genuine unresolved question, preserves the
   complete current deterministic baseline, and defines allowed pre-decision inputs.
2. The owner creates event-grouped/chronological partitions and commits exact dataset
   identities. The author receives only task, construction and tuning evidence.
   A separate reviewer retains held-out answers with enforced access separation.
3. Record author/model identity, model capabilities and evidence/parameter/token/edit
   budgets. Freeze deterministic alternatives before the first held-out access.
4. The author supplies complete weights, runs native construction-case checks, then
   makes only the bounded tuning edits. Record every candidate, native outputs,
   regressions, revision lineage, elapsed authoring time and available token measures.
5. Freeze the candidate artifact before the reviewer opens the held-out data. Evaluate
   exactly once for selection; later replays are regression checks. Reject harmful
   edits and retain rollback. Repeated independent author trials use identical evidence
   budgets and do not receive previous held-out feedback.
6. Compare a defensible deterministic improvement and conventional optimization when
   available through mncs-learn. Its inspected native implementation currently exposes
   centroid/no-learning contracts, not a neural-weight optimizer. No host optimizer
   or private learning-governance fork is added here to fake that baseline.
7. Report initial/final quality, edit success/regressions, parameter and inference
   cost, observed author time/tokens, maintenance burden and verified outcome costs
   separately. A one-weight edit is not inherently cheaper than an equivalent
   standalone-network edit. Do not derive causal operational savings from replay.

## Prior campaign readiness

A real labeled residual cohort and independently controlled held-out custody are
missing in the inspected sources. This author already knows the old synthetic
answers, so reusing those fixtures would not be a sealed authoring trial. No new
artificial utility benchmark substitutes for them. Token and author-construction
costs for a controlled trial remain unmeasured; CLI probe wall times are execution/
transport measurements, not authoring time. The smallest next work is owner-bound
data capture and custody for one task, followed by a bounded direct-weight trial.

The subsequent [test-priority evidence campaign](TEST_PRIORITY_EVIDENCE.md)
performed a source-bound native replay and added complete-alternative trial
evaluation. The all-pass, already-known source and missing independent changed
source groups do not establish an eligible training/held-out cohort. No authored
weight attempt is credited by reusing the old fixture vectors.
