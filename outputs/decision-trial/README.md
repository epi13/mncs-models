# Native test-priority eligibility replay

**Finding: no eligible real-data learned trial was established.** This campaign
ran a complete source-bound native replay, retained the strongest deterministic
source-relevance response, and added a small native complete-outcome evaluator.
It demonstrates no learned advantage, controlled direct-weight authorship,
information/capacity advantage, compositional advantage or agent-time saving.

## Outcomes and denominators

The unchanged published Models source matches the earlier complete guidance
receipt's source map and compiler binary. Its replay preserves all 71 tests.
A source snapshot and prior observations were then recorded in `plan.json` **before**
the support extension's final native results were read. That target snapshot also
passes the 71 preserved tests; 15 new mechanical replay tests separately pass.
These are two source snapshots, including a support extension, rather than 142
independent historical decisions. Old synthetic fixture labels remain synthetic.

| Operation | Tests | Prior observed VM steps | Target observed VM steps | Target suite CLI wall, s |
| --- | ---: | ---: | ---: | ---: |
| 1: foundation | 14 | 115,484 | 115,484 | 22.560 |
| 2: composition | 16 | 1,633,084 | 1,633,084 | 52.524 |
| 3: residual | 15 | 366,291 | 366,291 | 71.356 |
| 4: guidance | 26 | 27,488 | 27,488 | 42.499 |

Every candidate suite passed. Native `evaluate_initial_test` evaluated all four
possible initial choices and explicit abstention. Every complete result reports
zero failing candidates, `oracle_cost_known=false`, four mandatory executions and
**2,142,347** total measured VM steps. No failure latency exists to improve on this
source. Deliberately supplying only one candidate outcome returns `accepted=false`,
reason 2, and retains the supplied/required counts. It is a missing-evidence probe,
not another real decision or a learned abstention-rate estimate.

## Deterministic baselines

The pre-decision canonical least-prior-cost call selects guidance (operation 4,
27,488 steps); its actual native result is retained. Prior VM counts exactly match
target counts for this workload. There is no need to learn that known cost ranking.

Source identity and relevance precede cost. Unchanged verified inputs are excluded
from a learned target when the owner's reuse rules admit them. For the support
change, the only directly affected **preserved** suite imports `mncs.models.trial`:
residual. A source-only projection into the existing native guide selects operation
3. The new replay suite is additional direct-consumer validation; it remains
mandatory and is not hidden to improve this four-suite matrix. This relevance
baseline is a retrospective reproduction, expressly not a frozen held-out trial
or proof of an optimal failure-finding choice. The raw four-suite cost projection
alone is not called the strongest usefulness estimator. Neither rule claims to
predict a defect from source dependency alone.

The verification script actually ran the fixed full order foundation, composition,
residual, guidance, then the added replay validation. Its initial choice is not an
optimal-action label. The native baseline was a recorded suggestion, not live
learned routing. Counterfactual comparison is limited to pure native assertion
outcomes and body VM counts on the same source; compilation/cache wall time is
order-dependent and is not reconstructed by adding individual durations.

## Costs and scope

- Source/dependency/compiler and prior-receipt acquisition: **0.312 s**,
  one host observation; excludes Environment/Store entry and native calls.
- Native four-candidate cost baseline: **1,110 VM steps**, **21.244 s** CLI wall.
- Native source-relevance projection: **321 VM steps**, **4.730 s** CLI wall.
- Complete-outcome evaluation: **2,719 VM steps** per choice/abstention; first
  CLI call **28.115 s**, subsequent choice calls
  **6.136–6.326 s**. These are evaluation costs, not neural latency.
- Missing-alternative refusal: **1,158 VM steps**, **6.198 s** CLI wall.
- Final mechanical replay suite: **15 passing tests**, **44.002 s** complete suite wall.

All timings are descriptive, include their declared admission/cache/transport
scope, and are not isolated machine benchmarks. Raw calls and receipts retain all
measurements. VM steps, wall time, Store/environment burden and agent burden remain
separate. Environment entry/Store load, physical I/O, peak memory and causal agent
work reduction were not separately measured. No model was constructed or loaded;
parameter authorship/edit/maintenance costs are therefore **not measured**, rather
than an asserted zero-cost model. There is no trainable cohort on which to compare
five versus fifty parameters, complementary learned views or specialist composition.

## Evidence and reproduction

`source-inventory.json` records 16 repository checkout observations and foreign work.
`source-references.json` pins committed evidence, including the completed remediation
and its one supported native Test operation. `job-audit.json` retains 100 bounded
Control rows with explicit missing research joins; all lack upstream/result-summary/
artifact links in this returned inventory. It supplies no complete demand denominator
or decision-time permitted-operation set. Current captures are not replaced by
historical guesses. The native supported proof has one operation, not alternatives.

`plan.json` preserves pre-decision source/dependency/compiler digests, prior native
selection/outcome identities and observations. `reference-context.json` binds local
native handles to full artifacts. `baseline/` and `verification/` retain raw native
results, exact Test identities and source-bound receipts. `replay/` retains every
native argument/result; `replay-receipt.json` binds their bytes and costs.
`development/` retains the earlier 14-test support check before the budget regression
was added. `finding.json` makes unmeasured/not-conducted findings explicit.

Run `python3 scripts/verify.py --output-root outputs/my-check` for all **86 native
tests** without overwriting prior receipts. Exact native replay commands and typed
arguments are in the existing result files. A fresh two-phase study uses
`verify.py --output-root outputs/new-study/baseline`, then
`measure_test_replay.py --output-root outputs/new-study --prepare`, final verification
with `--output-root outputs/new-study/verification`, and finally
`measure_test_replay.py --output-root outputs/new-study --evaluate`; the
published plan deliberately refuses replacement. Use an isolated output campaign
for a new study rather than rewriting this evidence.

See `docs/TEST_PRIORITY_EVIDENCE.md` for the complete decision definition, rejected
candidates, custody limits and the least additional changed-source outcome evidence
needed before a real direct-weight trial. Only Models source changed; no live model
consumer, telemetry service, second runtime or optimizer was introduced.
