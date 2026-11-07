# Agent demand: read-only evidence audit

This phase inspected naturally recorded development activity before proposing a
learned guide. It found concrete historical deterministic delivery deficiencies,
but no defensible cohort demonstrating avoidable agent work or a useful learned
selection. No operational behavior was changed for this audit.

The bounded source archive and commit/digest manifest are in
[`outputs/guidance/observations`](../outputs/guidance/observations/manifest.json).
Repository bytes were checked against the recorded commit before packaging.
Embedded historical claims and their supporting pointers were not independently
replayed or recursively reauthenticated. This is an audit of accessible evidence,
not a census of MNCS activity.

## Available observations and their limits

| Authority / source | Directly available | What it does not establish |
| --- | --- | --- |
| Control `terminal_jobs` | 100 server-owned retained jobs, October 17–November 6, 2026; returned/redacted command, sandbox cwd, project, start/completion timestamps, exit/status, upstream/artifact fields | Complete sessions, all terminals, agent reasoning time, decision-time repository identity, tool usefulness, or independently verified source outcomes |
| Control `terminal_output` | Six selected jobs read by their returned IDs | All six returned empty stdout/stderr with `output_truncated=false`. This does not mean the original commands printed nothing. No diagnostic cause can be reconstructed from this readback. |
| Environment session activity | Bounded invocation/completion/read-operation events, objective/context references, checkout observations, explicit-invoke surface markers, source digests and paging limits | Direct shell/search tools outside Environment bindings; a CLI marker does not identify an actor or a missed ambient opportunity |
| Environment capability delivery | Binding snapshots, context-response set inclusion/digests, declared versus callable addresses | Receipt, relevance, use, or sufficient information at the agent's decision time |
| Environment owner-pass trace / service accountability | Scheduled/skipped dispositions, input-chain refusal reasons, execution/result links, elapsed time and selected scheduler-process counters; bounded readiness-probe coverage | Agent-need denominator, fulfilled needs, independently verified work, intervention savings; child costs are excluded where the contract says so |
| Environment source/evidence projections | Exact repository/commit/path/digest references, source schema adapters, recorded verification and scoped outcomes | A complete deployment inventory, causation, historical availability from current bindings, or benefit from a record merely being displayed |
| Forge / Actions / Test | Execution and verification receipts with subject/run/result scope; native tests and result validity remain their authorities | A successful execution receipt alone is not a verified claim or a useful diagnostic. The previous selected Forge audit found no suitable labeled cohort; this phase does not reinterpret that as a whole-system finding. |
| Doctor / Fabric | Health and worker/execution projections and source-owned receipts | A worker condition causing a later failure, or a diagnostic invocation resolving an agent's question |
| Language Service / LSP, RAVEL | Language-owned event cursors/subject identities and bounded semantic deltas are consumed by Environment; RAVEL declares snapshot-bound task/evidence/provider contracts | A retained per-agent search/LSP/context-request history joined to later usefulness was not obtained. No next-request training cohort is inferred from source contracts. |
| Git | Current refs and source history; Environment observes selected ref transitions | Remote publication from a local ref change, accepted changes from shell exit alone, or authoritative historical state for an unrelated terminal job |

The Control inventory is bounded at 100 records; its response supplies no complete
history or omitted-count guarantee. `running=0` concerns this server's inventory.
Selected records have null upstream IDs and empty artifact lists. Sandboxed
`/workspace/...` cwd strings were preserved; they were not equated with a host
checkout or HEAD by pathname similarity. Local `exec_command` work in this run is
not assumed captured there. Personal logs, prompts, conversations, and home-directory
agent traces were not inspected.

Read-only inspection of Control at `f5915e679e9af969770aa23f4947225525422175`
identifies a precise observation-contract deficiency: restored job metadata leaves
the stdout/stderr buffers absent, while `output()` maps an absent buffer to empty
text, offset zero and `output_truncated=false`. That is compatible with the six
observed readbacks, but does not prove the deployed service ran this revision or
that a restart caused those particular responses. The returned contract does not
distinguish an unavailable capture from an actually empty capture. The same source
caps persisted/reloaded/listed job rows at 100. A deterministic capture-availability
field is a better response to this ambiguity than learning causes from exit codes.

Control source also declares an aggregate `audit_summary` and a project-scoped
redacted journal projection. Neither was exposed in this session's available tool
catalog. Their private backing audit log was not opened as a fallback. Language
Service at `060b7898bbfb823f4e8a8ba32658fc35be2c96ec` supplies resident semantic
deltas and language-capability queries, with bounded cursors and explicit history
reset/UNKNOWN; these are knowledge/event projections, not evidence that an agent
needed, received or successfully used a query. The manifest pins these source
inspections without claiming a deployed build identity.

The task-owned Environment readback is separately archived as
`selected-session-services.json`: session `ses_ff95f7f9e223ce3d`, snapshot 13,
event sequence window 2–5, older records present, truncated window, status
`partial-no-invocations-in-selected-window`. Its empty declared service scope has
`eligible_service_opportunity_count=null`, agent receipt/outcome quality
`not-established`, and intervention burden `not-measured`. Zero declarations
and zero selected invocations are not a 100% fulfillment score. This new session
documents interface behavior, not an independent historical development workload.

## Reconstructed workflows

### 1. Exact context needed for a campaign read

The archived `compiler-project-context-selection-recurrence-20261024.json` records
an observer pursuing Compiler campaign evidence in campaign
`cmp_mncs_native_application_readiness_compiler_20261013`, session
`ses_164edc158d9b1637`, checkpoint `chk_691079cfe830f05d` (649).

1. A `campaign_state` read from project cwd `.` supplied a known campaign/session
   and received `ENVIRONMENT_SESSION_SELECTION_REQUIRED`: multiple registered
   worktrees required checkout context. No continuation was returned.
2. Supplying the exact registered nested worktree enabled the read of evidence
   offset 692, limit 1, returning the intended Compiler evidence identity.
3. Successful reads are linked to `evt_d8e6087624167b5a` / `rpc_e15792ae5024c6a0`
   at 14:30:55 UTC and `evt_fb91255bfddb5464` / `rpc_50945b176e877663`
   at 14:31:28 UTC. Dispatch durations were 12,785.62 and 21,152.21 ms.

These were the historical observer's context reads, not Compiler implementation
or verification runs. Dispatch includes queue wait. The failed read's exact
event time, live branch/HEAD, complete preceding search sequence, agent tokens
and agent duration are absent. The later read independently identifies a returned
record within the owner-recorded history; it does not show how long a different
entry path would have taken.

**Supported conclusion:** exact-context delivery was a concrete deterministic
service limitation at that boundary. Return required authenticated checkout
context or honor a uniquely authorized selector, retaining all ownership checks.
There is no reason to learn which worktree the caller is authorized to use.
The source labels recurrence across independent campaigns unestablished. Do not
count its two reads as two independent defect occurrences or as redundant work.
Later source changes may already address parts of this limitation; a current
reproduction must precede any proposed owner fix.

### 2. Real compiler measurements missing from an evidence projection

At 18:40:48 UTC on October 24, the archived domain-projection pressure record
reports a bounded eight-record campaign page containing a digest-addressed Compiler
regression record, while the Environment observation view exposed zero references.
The record included measured build-resource and verification-fact reuse evidence.

The later language-fact improvement record links a schema-aware deterministic
adapter at `2a5e8f5675b3cbf196f8935579ceee00e6866afa`. It separated 13 reused
structural dependency summaries from 12 Language verification facts. The
19:08:32 canonical readback reports four verified observation records, eleven
integrity-verified source pointers, a validated improvement relation, and **partial**
projection status. At that readback the follow-up record was not yet present.
Production exposure and later agent outcomes were expressly unestablished.

**Comparison supported by these owner records:** baseline source-format delivery
gap versus verified deterministic projection/adaptation. This is a service
correctness improvement, not a measured reduction in searches, tokens, diagnostic
work or escalation. No model was needed to recognize a supported source schema.

### 3. Naturally occurring terminal retries: activity without causal context

Two October 30 jobs share cwd, consumer and task selector:
`term-b2c1b16cdfc0227bc20dfa5d` attempted Environment entry without a campaign
selector and exited 2; `term-aad094f8d9af4fc4df630cd6` added an explicit campaign
selector and exited 0. Their process intervals are recorded; no preserved output,
source-state binding, result artifact or authenticated common decision ID was
returned. The second exit does not prove the added flag caused success, or that
the intended development task completed.

Two October 25 jobs, `term-fbf91065a74bec7f0d95970b` and
`term-ca7cb806f17a40f0bd65d91b`, repeat an identical entry command and both exit 3.
Retries after failure can be legitimate. Their similarity does not establish
redundancy. A selected October 21 compound continuation/push command exited 0;
that alone supplies no commit or remote identity for independent verification.

**Classification:** insufficient evidence. These are candidate demand sequences,
not outcome-aligned examples for training, avoided-call credits, or complete agent
sessions. The native `partial_workflow` probe is a missing-join analogue with local
handles, not an authenticated import of these records.

## What existing ambience measurements actually count

Environment's capability-intelligence contract already separates declarations,
address resolution, delivery-set inclusion, recorded invocation/completion, owner
decisions, verification evidence, and fulfillment. It preserves unknowns instead
of claiming a general ambience score. The October 27 owner-pass improvement
linked scheduler results to service-accountability by exact snapshot/digest;
the live readback retained partial/truncated status and unassessed effectiveness.
An earlier interrupted entry recorded 26 completed capability calls, including
18 Doctor projection-health calls. Its evidence explicitly does **not** establish
that those calls were redundant, caused I/O, or represented agent needs.

Useful denominators remain different:

- Readiness probe coverage: uniquely matching valid observations / declared probe
  opportunities. It measures recorded probe coverage.
- Scheduler decision coverage: recorded decisions / declared owner passes in the
  selected trace. It measures trace coverage.
- Delivery-set inclusion: bindings in a context response / bounded binding snapshot.
  It measures delivery membership, subject to truncation.
- Fulfilled demand: would require useful, current, sufficient support delivered for
  a particular eligible need, followed by independently verified work. The inspected
  records do not supply that denominator or a verified numerator.

No denominator above should silently become another. Current feature availability
must not be backfilled into historical decisions. Missing pages are neither failed
service nor fulfilled demand. Current observations need an owner-defined freshness
rule; matching a state ID alone is not a guarantee of real-world freshness.

## Prioritized owner improvements and honest next evaluation

| Priority / response | Owner and minimum evidence | Success criterion |
| --- | --- | --- |
| 1. Distinguish absent capture from empty output | Control: existing job identity/metadata and bounded capture lifecycle (retained, restored-without-capture, aged, or genuinely empty); no prompt or raw audit-log collection | Empty historical readbacks report explicit availability; missing logs cannot become evidence that a command emitted no diagnostics. Verify restart and bounded retention behavior in the owner's tests. |
| 1. Deterministic context delivery | Control + Environment: explicit authenticated campaign/session/task, exact registered checkout, conflict outcome and required selector; inspect existing corrections first | Intended record can be obtained from supported entry context without weakening ownership; preserve ambiguous/symlink/unrelated-clone refusal. Measure subsequent ordinary-agent requests separately. |
| 2. Preserve source meaning in compact projections | Environment with Compiler/Language evidence owners: exact source schema, commit/digest, supported scoped outcome, adapter verification, actual delivered view | Supported evidence and its limits survive compaction. Existing adapters are a verified partial solution; measure later consumption before claiming burden reduction. |
| 3. Join existing activity to decision opportunities | Environment owns correlation; Control supplies server job IDs, result/capture availability, caller-supplied task/checkout references where already authorized | For naturally occurring requests, retain a bounded decision ID, observed-before timestamp/sequence, exact state and permitted capability snapshot, delivery/result links, capture-availability reason, and independently verified follow-up. No prompt interception or new service. |
| 4. Evaluate deterministic service before learning | Environment + Test/Forge: predeclared comparable task/state cohort, actual existing path, deterministic alternative and verified result/cost | Report outcome-preserving completed work and measured extra/avoided operations. Failed/skipped required verification cannot count as savings; wall gaps cannot count as reasoning time. |
| 5. Conditional micro-model candidate | Test/Forge or context provider with Environment: unresolved selection among multiple legitimate diagnostic/test/context capabilities, pre-decision features, actual useful-evidence result, complete cost/outcome references | First show a remaining selection error/avoidable escalation after the improved deterministic baseline. Only then use disjoint construction/tuning/sealed test groups and compare a tiny guide with the same information. |

Novel design, interpretation and independent verification remain agent work unless
stronger evidence establishes otherwise. Next-command prediction would measure
behavioral demand only; it could reproduce inefficient sequences. Useful-evidence
prediction needs independently established usefulness. Causal savings require an
authorized controlled comparison or legitimate deterministic replay, not an
unobserved alternative action. No such utility cohort or replay was established
here, and no controlled LLM weight trial was conducted.
