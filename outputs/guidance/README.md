# Guidance verification and observation evidence

Reproduce with `python3 scripts/verify.py --suite guidance`; use the default
invocation to preserve/check the complete 71-test boundary. All classification,
selection and outcome semantics execute in native MNCS. Python transports native
test/call requests and packages receipts only.

`receipt.json` binds native results/probes to all repository MNCS source digests
and the actual compiler binary digest. Observed toolchain checkout heads are not
binary build attestations. `native-result.json` contains the 26 test results.
The six callable JSON results retain complete native returns and VM step counts.
Wall time in the receipt includes compilation/cache/CLI/transport overhead.

| Complete native probe | VM steps | Observed CLI wall seconds |
| --- | ---: | ---: |
| Reviewed demand classification | 360 | 8.851 |
| One candidate | 388 | 8.782 |
| Two candidates | 668 | 8.786 |
| Eight candidates | 2,992 | 8.862 |
| Established two-candidate bypass | 529 | 8.803 |
| Incomplete-history refusal | 152 | 8.781 |

These are one recorded invocation per probe, not latency distributions. The
bypass fixture includes an unavailable unchosen candidate and unknown selected
cost; it is not an otherwise identical treatment for a causal timing comparison.

`observations/manifest.json` pins the separately archived read-only activity
evidence. It is not a training dataset, a complete history, or a utility result.
The selected terminal outputs contain no retained diagnostics. Historical owner
evidence records source projection and context-delivery improvements, with their
original partial/unknown and unmeasured-benefit limits intact.

The numerical model/composition runtime and previous negative findings are
unchanged. The prior `outputs/residual/stages.json` is retained as historical
stage evidence from the preceding phase; it is not claimed as a newly completed
stage measurement. New complete guidance calls are measured here. The full run
also rechecks the original composition benchmark and callable costs.

There are no trainable parameters, model invocations or graph rows in this guide.
One/two/eight-candidate fixtures materialize exact arrays of those lengths and
borrow actual-length bounded views. Admission uses n row checks and n² identity
comparisons (at most 64), then one bounded ranking pass. Established selection
bypasses ranking/cost estimation, while retaining membership/contract admission.

Each candidate declares eight u64 fields (64 integer payload bytes), two booleans
and one finite status through its evidence record. The boundary declares eight
u64 fields; the problem adds four plus the view. The returned Guidance declares
seventeen u64 fields and a boolean. These field inventories include metadata,
not just numerical work. They do **not** establish physical allocation bytes:
finite tags, boolean representation, alignment, view descriptors, backing retained
by arbitrary callers, VM records/arena/stack and compiler artifacts are additional.
Peak runtime memory and pure inference latency were not measured. Nothing treats
the parameter-free guide as free execution or equates VM steps with agent burden.

See [native contracts](../../docs/DECISION_GUIDANCE.md) and
[the real-workflow audit](../../docs/AGENT_BURDEN.md) for interpretation and next
owner observations. No learned-guide benefit, causal savings, controlled LLM trial
or operational integration is established by these results.
