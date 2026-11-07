# Roadmap

## Ambient demand and operation-guidance milestone

- [x] Bounded read-only audit of retained Control jobs and Environment evidence/projections.
- [x] Reconstruct source-recorded context-selection and compiler-evidence delivery workflows, preserving timing/correlation limits.
- [x] Native six-category demand projection with reviewed sufficiency, joins, timing and exclusions.
- [x] Native 1–8 candidate deterministic-operation selection, exact permitted-set references, cost units/budgets, bypass and abstention.
- [x] Separate actually selected operation/usefulness/work-verification/call-count outcomes.
- [x] Preserve 45 tests and historical results; add 26 native tests and complete-call probes.
- [x] Owner-specific deterministic improvements and precise missing opportunity/outcome observations documented.
- [ ] Naturally occurring, independently verified demand/decision cohort with decision-time state and capability delivery.
- [ ] Measured outcome-preserving reduction in agent work from deterministic service improvements.
- [ ] Learned operation guide, only after a remaining uncertainty and same-information deterministic baseline justify it.

No live guidance, telemetry service, LLM weight trial or operational benefit is claimed.
See [AGENT_BURDEN.md](docs/AGENT_BURDEN.md), [DECISION_GUIDANCE.md](docs/DECISION_GUIDANCE.md) and RFC 0005.

## Residual/proportional execution milestone

- [x] Native model-free residual gate; established answers bypass inference.
- [x] Specific question/model/feature bindings, pre-decision timing and explicit fallback.
- [x] Separate observed outcome accounting and separate-unit utility comparisons.
- [x] One Model with compact immutable parameter updates and fresh bucket backing.
- [x] Active-lane numerical execution; remove duplicate same-call model validation.
- [x] Qualified projected DAG admission and four-item lexical admission reuse.
- [x] Preserve thirty tests and negative historical findings; add fifteen native tests.
- [x] Source-bound construction/admission/inference/revision stage measurements.
- [x] Native direct-weight interchange and disjoint/frozen trial bookkeeping.
- [x] Bounded read-only operational evidence audit: no suitable labeled cohort found in the inspected context.
- [ ] Real residual utility and controlled LLM weight-engineering trial: cohort/custody missing.
- [ ] Unforgeable admission reuse across arbitrary calls; no unchecked certificate substituted.
- [ ] Peak native memory and graph-rebind maintenance measurements.

Do not raise node capacity or deploy models before these costs and utility are justified.
See [RESIDUAL_INTELLIGENCE.md](docs/RESIDUAL_INTELLIGENCE.md) and RFC 0004.


## Verified composition milestone

- [x] Reuse native Model/infer in a bounded DAG with explicit contracts.
- [x] Independent local models, deterministic and learned glue, component edit/rebind/rollback.
- [x] Missing/contradictory/abstaining output propagation and numerical/resource refusal.
- [x] Two/three-node constructions and a reusable connected ten-node sensor construction.
- [x] Frozen 32-case synthetic comparison, including a harmful tuning edit and superior deterministic baseline.
- [x] Active and allocated resource accounting with native execution measurements.
- [x] Compact editable parameters via exact 5/20/100-slot materialization; direct view replace remains refused with MNE198.
- [ ] Matched LLM intervention-cost experiment and authorized real-trace evaluation.
- [ ] Larger assemblies, after storage/validation overhead is measured and improved.

Details and limitations: [COMPOSITION.md](docs/COMPOSITION.md), RFC 0003.
This does not complete the broader graph, sharing, recurrence, routing or operational phases below.


Current executable boundary: [native micro-model foundation](docs/NATIVE_FOUNDATION.md). RFC 0002 records the implemented slice; broader graph and operational interfaces below remain design targets.

This roadmap is ordered to make `mncs-models` a native model-construction layer rather than a new host-language ML framework.

The phases are implementation milestones, **not parallel product versions**. The repository should maintain one canonical implementation and migrate it forward as each milestone is reached.

## Foundation — repository boundary and architectural charter

Goal: establish what `mncs-models` owns before implementation choices narrow the design.

- [x] Define the repository as the canonical MNCS model construction/composition layer.
- [x] Retire the all-in-one MNEL ownership model for model construction.
- [x] Establish composition-first rather than named-architecture-first design.
- [x] Make routing, recurrence, parameter sharing, sparse activation, and heterogeneous composition first-class requirements.
- [x] Separate model structure from learned parameter/state artifacts.
- [x] Establish family ownership boundaries.
- [x] Establish the one-canonical-implementation rule.
- [x] Establish research intake discipline.
- [x] Record the initial architecture RFC and known implementation pressures.

## Phase 1 — family and language contract discovery

Goal: derive the first executable model contract from the capabilities that actually exist across MNCS today.

- [ ] Inspect current `mncs-language`, compiler, runtime, and Commons capabilities relevant to model graphs.
- [ ] Inspect `mncs-learn` contracts for addressable model targets, topology, routing, and parameter/state mutation.
- [ ] Inspect `mncs-memory` interfaces for memory-conditioned model components without duplicating memory semantics.
- [ ] Inspect `mncs-store` artifact/state identity and persistence contracts.
- [ ] Inspect `mncs-ingest` typed observation/data interfaces relevant to model inputs.
- [ ] Inspect rights/provenance contracts that model artifacts and construction inputs must preserve.
- [ ] Inspect Fabric/execution capability descriptors relevant to model requirements without importing scheduling policy here.
- [ ] Identify reusable identities/types already owned by `MNCS-Commons`.
- [ ] Produce concrete language/runtime pressure findings instead of guessing what is missing.
- [ ] Update the RFC and architecture document with the discovered contract.

Deliverable: a reviewed implementation plan grounded in current repository heads, with every proposed host scaffold justified by a specific missing native capability.

## Phase 2 — canonical model graph

Goal: establish the smallest native representation that can describe a useful model composition.

Required concepts should be validated by implementation pressure, but likely include:

- [ ] model identity and metadata;
- [ ] typed external interfaces;
- [ ] addressable components/submodels;
- [ ] typed ports and connections;
- [ ] parameter declarations;
- [ ] mutable/persistent state declarations;
- [ ] transient/runtime state declarations;
- [ ] explicit parameter/state sharing or aliasing;
- [ ] nested composition;
- [ ] structural validation;
- [ ] deterministic structural identity/digest where semantics permit it;
- [ ] external artifact references without embedding storage semantics.

Demonstration target: construct and validate a small feed-forward model from reusable components and address every component/parameter declaration deterministically.

## Phase 3 — compact specialist models

Goal: prove that the representation works for the small-model side of the original MNEL thesis.

- [ ] compact classifier/reference predictor;
- [ ] multiple specialists with distinct typed inputs or declared specializations;
- [ ] parallel execution structure;
- [ ] deterministic aggregation;
- [ ] parameter sharing across selected specialists where meaningful;
- [ ] model-stack composition from independently defined submodels;
- [ ] construction manifest that does not require embedding learned weights.

Demonstration target: a small parallel specialist/classifier stack assembled from common primitives rather than a special ensemble runtime.

## Phase 4 — routing and conditional computation

Goal: make dynamic path selection a structural capability rather than a framework-specific callback.

- [ ] router/gate representation;
- [ ] sparse activation semantics;
- [ ] top-k or bounded selection structure without hard-coding one routing algorithm into the ontology;
- [ ] conditional branches;
- [ ] early-exit/readout paths;
- [ ] aggregation/merge semantics;
- [ ] capacity/bounds declaration where required;
- [ ] learning-addressable routing state without moving learning policy into this repo.

Demonstration target: route one input through a subset of parallel specialists, aggregate their outputs, and expose the routing structure to `mncs-learn` and verification tooling.

## Phase 5 — sequence mixing and transformer constructions

Goal: prove that common transformer-style models emerge from the shared representation.

- [ ] sequence/token representation interfaces as needed;
- [ ] attention/mixing primitive or generic mechanism capable of representing it;
- [ ] feed-forward/transform composition;
- [ ] normalization/residual structure;
- [ ] positional/ordering state or interfaces where required;
- [ ] multi-head or parallel mixing composition without architecture-specific duplication;
- [ ] reusable block composition;
- [ ] output/readout heads.

Demonstration target: express a compact transformer-like reference model entirely through general model primitives.

## Phase 6 — recurrence, loops, and adaptive depth

Goal: ensure repeated computation is represented semantically rather than by copying an unrolled stack.

- [ ] recurrent region/loop semantics;
- [ ] shared parameters across iterations;
- [ ] recurrent stateflow;
- [ ] bounded iteration declaration;
- [ ] adaptive halting/continuation interface;
- [ ] per-iteration outputs or inspection hooks where meaningful;
- [ ] nested recurrence constraints;
- [ ] deterministic structural identity independent of an arbitrary unroll count when appropriate.

Demonstration target: express a recurrent-depth/looped transformer-style model using the same block definition across multiple computation steps.

## Phase 7 — recurrent, state-space, and hybrid sequence models

Goal: avoid making attention the only first-class sequence mechanism.

- [ ] recurrent state transition components;
- [ ] state-space/scan-like composition where supported;
- [ ] selective or gated state update structure;
- [ ] explicit long-lived vs transient sequence state;
- [ ] hybrid attention/state-space stacks;
- [ ] shared interfaces allowing different sequence mixers inside the same higher-level model.

Demonstration target: construct attention, recurrent/state-space, and hybrid sequence models without forking the model ontology.

## Phase 8 — experts and heterogeneous sparse stacks

Goal: support MoE-style and more general heterogeneous expert systems.

- [ ] expert-set abstraction from general submodels;
- [ ] homogeneous and heterogeneous experts;
- [ ] router/expert capability matching;
- [ ] sparse activation bounds;
- [ ] shared/private parameter declarations;
- [ ] expert aggregation;
- [ ] fallback/no-route semantics;
- [ ] externally visible expert identity for learning, provenance, and inspection.

Demonstration target: one stack containing experts with meaningfully different internal structures selected through the common routing contract.

## Phase 9 — multimodal and multi-path composition

Goal: make modality-specific and cross-modal models ordinary compositions.

- [ ] typed modality interfaces without hard-wiring a closed list of modalities;
- [ ] private modality encoders/paths;
- [ ] shared latent representations where appropriate;
- [ ] cross-modal mixing/fusion;
- [ ] modality-specific experts or heads;
- [ ] missing/optional modality structure;
- [ ] shared/private parameter relationships;
- [ ] nested submodels constructed independently and composed later.

Demonstration target: a multimodal stack with independently constructed modality paths and an explicit fusion/readout structure.

## Phase 10 — learning, memory, ingest, store, and provenance handshake

Goal: prove that `mncs-models` is a usable family contract rather than an isolated schema.

- [ ] `mncs-learn` can address model parameters/state/topology/routing through stable identities.
- [ ] learning-driven topology changes can produce a replacement canonical model graph without creating version forks.
- [ ] `mncs-store` can persist/retrieve model definitions and external parameter/state artifacts.
- [ ] `mncs-memory` can satisfy declared memory interfaces without its semantics being copied here.
- [ ] `mncs-ingest` outputs can bind cleanly to model inputs.
- [ ] rights/provenance lineage can follow model construction sources and learned artifacts.
- [ ] deterministic construction/replay can recreate the same structural identity from the same declared inputs.

Demonstration target: ingest -> model -> governed learning proposal -> stored updated model/state -> reload/reconstruct, with provenance intact and repository boundaries preserved.

## Phase 11 — portable compilation and execution

Goal: make one model contract consumable by multiple execution strategies.

- [ ] compile/realize the same model description through appropriate MNCS compiler/runtime paths;
- [ ] capability requirements are declared separately from placement decisions;
- [ ] CPU reference execution for bounded examples;
- [ ] accelerator realization where useful and supported;
- [ ] distributed/fabric execution without model-semantic changes;
- [ ] consistent component identities across realizations;
- [ ] backend-specific optimizations remain semantically equivalent or explicitly declare approximation.

Demonstration target: execute the same canonical model graph through at least two materially different realizations while preserving observable model semantics and identity mapping.

## Phase 12 — architecture construction as a machine-native activity

Goal: allow MNCS to construct and revise model topologies from the same primitives used by humans.

Research targets:

- [ ] model-template parameterization;
- [ ] constrained architecture search;
- [ ] machine-generated compositions subject to type/resource/capability constraints;
- [ ] learned component selection;
- [ ] learned depth/width/expert allocation;
- [ ] model split/merge/replacement proposals through `mncs-learn`;
- [ ] architecture distillation/compression as graph transformation;
- [ ] structural comparison and equivalence/compatibility analysis;
- [ ] utility/resource-aware model construction;
- [ ] provenance of machine-generated architecture decisions;
- [ ] replayable construction decisions and deterministic manifests.

This phase should not proceed by adding opaque AutoML machinery. Architecture construction should operate on the same explicit model primitives and governance boundaries as ordinary model definition.

## Continuing research track

Architecture research runs across every phase rather than after implementation is "finished."

Continuously evaluate developments in:

- parallel specialist and classifier systems;
- sparse/conditional computation and routing;
- mixtures of experts;
- looped/recurrent-depth transformers;
- adaptive computation/halting;
- recurrent and state-space models;
- hybrid sequence architectures;
- multimodal specialization/fusion;
- graph/relational neural models;
- memory- and retrieval-conditioned models;
- autoregressive, diffusion, flow, energy-based, and other generative structures;
- continuous-time/neural differential models where useful;
- architecture search, compression, distillation, and self-composition.

The output of research is not automatically code. It should produce one of:

1. evidence that existing primitives already represent the architecture;
2. a concrete missing primitive/constraint;
3. an implementation pressure for another MNCS repository;
4. a bounded reference construction;
5. a documented decision that the idea is not currently useful.

## Cross-cutting definition of progress

A change is meaningful progress when it improves one or more of these without degrading the others unnecessarily:

1. **native expression** — more authoritative model semantics live in MNCS rather than host shadows;
2. **composability** — more architectures emerge from reusable primitives;
3. **heterogeneity** — different model families coexist in one graph/stack;
4. **addressability** — learning, storage, debugging, and provenance can name precise model structures;
5. **reproducibility** — construction inputs and structural identity are deterministic where possible;
6. **dynamic capability** — recurrence, routing, sparse activation, and adaptive computation remain explicit;
7. **portability** — model semantics survive backend/device changes;
8. **boundary health** — other MNCS repositories keep ownership of their domains;
9. **debt reduction** — superseded scaffolding is removed rather than preserved as another implementation generation;
10. **research absorption** — genuinely useful architectural advances can be represented without redesigning the repository around each paper name.
