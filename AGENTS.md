# AGENTS.md

## Mission

`mncs-models` is the canonical MNCS layer for **model construction and composition**.

Preserve this invariant:

> A model is an explicit, typed computational structure assembled from composable primitives. Named architectures are reference constructions, not the repository ontology.

The repository exists to define what a model is structurally and how model structures compose. It does not own the surrounding learning, ingestion, memory, storage, rights, orchestration, or deployment machinery.

## Before changing code

A fresh agent must not begin by inventing a framework in isolation.

Before implementation work:

1. Read `README.md`, the RFCs, `docs/ARCHITECTURE.md`, `docs/INTEGRATION.md`, `ROADMAP.md`, and `docs/RESEARCH_DIRECTIONS.md`.
2. Inspect the current heads, docs, RFCs, and public contracts of the MNCS repositories that touch the intended change, especially `mncs-language`, `MNCS-Commons`, `mncs-learn`, `mncs-memory`, `mncs-ingest`, `mncs-store`, `mncs-rights-provenance`, `mncs-actions`, and execution/fabric repositories as relevant.
3. Determine what can already be represented natively in MNCS and what is a genuine language/runtime pressure.
4. Prefer extending general MNCS capabilities in their owning repository over growing private shadow semantics here.
5. Keep implementation proportional to the pressure being solved. Do not build a large speculative framework simply because the model domain is large.

## Required architectural invariants

1. **Composition over architecture silos.** Transformers, state-space models, MoE systems, recurrent-depth models, specialist ensembles, multimodal models, and future designs should share common primitives where their semantics are genuinely shared.
2. **Model structure is explicit.** Components, connections, ports, state channels, parameter declarations, sharing, recurrence, routing, and submodel composition must not be hidden inside opaque host callbacks.
3. **Structure and learned state are distinguishable.** Model semantics must not depend on parameter bytes being embedded directly into topology definitions.
4. **Parameter sharing is first class.** Weight tying, block reuse, recurrent-depth sharing, expert sharing, and other aliases must be representable without duplicating state.
5. **Recurrence is first class.** A loop or recurrent region is not merely an unrolled stack copied N times.
6. **Routing is first class.** Conditional computation, expert selection, early exit, branch selection, sparse activation, and parallel specialist paths must have explicit structural semantics.
7. **Heterogeneous composition is valid.** A model stack may contain components with different internal computational families when their interfaces compose.
8. **Model interfaces are typed and inspectable.** Inputs, outputs, state, capabilities, and external dependencies should be machine-addressable rather than convention-only strings.
9. **Model identity is reproducible.** Equivalent structural constructions should be capable of deterministic identification when the participating semantics are deterministic.
10. **Execution placement is not model semantics.** A model may declare requirements or preferences, but worker/device scheduling belongs elsewhere.
11. **Learning is not owned here.** `mncs-models` exposes structures that `mncs-learn` can address and mutate through governed learning contracts; it does not duplicate the learning lifecycle.
12. **Storage is not owned here.** Model definitions may reference parameter/state artifacts, but `mncs-store` or another owning subsystem persists them.
13. **Memory is not reimplemented here.** Models may contain memory interfaces or memory-conditioned components; `mncs-memory` owns memory semantics.
14. **Rights and provenance remain enforceable.** Model manifests should carry or reference identity/provenance hooks required by the owning rights/provenance systems without duplicating their policy logic.
15. **No hidden host-language authority.** Host code may bootstrap or provide a backend, but authoritative model semantics should migrate toward native MNCS expression as the language becomes capable.

## One canonical implementation

Do not create artificial implementation generations.

At the current stage, the MNCS family is under coordinated development and its consumers can be migrated when a model contract improves. Therefore:

- evolve the canonical implementation in place;
- update affected MNCS consumers together when necessary;
- remove superseded scaffolding once the replacement reaches or exceeds it;
- move genuinely useful historical/reference implementations to an appropriate reference-study location rather than keeping them in the production path;
- do not create `v1`, `v2`, `legacy`, `next`, `old`, or parallel compatibility trees unless a real external compatibility obligation requires them.

Serialized artifact revisions may need explicit schema/revision identifiers. That is not the same as maintaining multiple product implementations.

## MNCS-language pressure

The desired end state is native MNCS representation of model contracts and critical construction/validation semantics.

Until a concept is expressible correctly:

- use a small bootstrap representation only when it makes the missing capability concrete;
- mark host/transport scaffolding as bootstrap or backend material rather than normative semantics;
- record the pressure in `ROADMAP.md`, an RFC, or an issue;
- do not invent unsupported `.mncs` syntax and describe it as working;
- do not permanently work around a missing general language primitive with repository-specific host logic when fixing the language is the healthier architecture.

Likely language/runtime pressures include typed graph structures, tagged component kinds, shape/type constraints, recursive or repeated composition, parameter aliasing, deterministic structural serialization, addressable nested components, conditional routing, and bounded dynamic execution. Treat these as hypotheses until verified against current `mncs-language`.

## Research intake rule

New model research is welcome, but paper names do not automatically become core abstractions.

For a candidate architecture or mechanism:

1. Identify the actual new semantic capability.
2. Try to express it with existing primitives.
3. If that fails, isolate the smallest general primitive that is missing.
4. Show at least one additional plausible use beyond the originating paper/architecture when claiming the primitive is general.
5. Separate architecture semantics from training recipe, benchmark setup, hardware trick, and implementation optimization.
6. Record uncertainty when a paper or implementation has not been independently validated.
7. Prefer a compact reference construction over cloning a full external framework into this repository.

Examples:

- A new looped transformer should pressure recurrence, parameter sharing, halting/adaptive-depth, and stateflow primitives before creating a special `LoopTransformer` ontology.
- A new MoE variant should pressure routing, expert sets, capacity, aggregation, and sparse activation semantics before creating a one-off family hierarchy.
- A multimodal model should pressure typed modality paths, shared/private parameters, cross-modal mixing, and composition interfaces rather than becoming an isolated multimodal runtime.

## Integration ownership

Keep these boundaries explicit during design and code review:

- `mncs-models`: model structure, composition, construction, structural identity, model manifests, architecture recipes/reference constructions.
- `mncs-learn`: evidence-governed changes to parameters, state, routing, relationships, and topology.
- `mncs-ingest`: external/raw input to typed evidence/observations.
- `mncs-memory`: persistent/working/episodic/semantic memory behavior and retrieval semantics.
- `mncs-store`: durable model/state/artifact storage and retrieval.
- `mncs-rights-provenance`: rights, provenance, lineage, and usage constraints.
- `MNCS-Commons`: shared cross-family identities/types/contracts where appropriate.
- `mncs-language` / compiler / runtime: native representation and generic executable semantics.
- `mncs-fabric` and related execution systems: worker/device placement and distributed execution.
- `mncs-actions`, `mncs-test`, `mncs-debug`, `mncs-doctor`, `mncs-forge`: verification, diagnostics, conformance, orchestration, and development machinery.

If a change begins absorbing another repository's responsibility, stop and define the interface instead.

## Change discipline

For a semantic change to model contracts:

1. update the relevant RFC/design document in the same change;
2. state the invariant or pressure motivating the change;
3. identify integration impact on other MNCS repositories;
4. add or update machine-verifiable invariants once an executable representation exists;
5. migrate the canonical implementation and known consumers rather than creating a permanent compatibility fork;
6. remove obsolete code/docs when the new path supersedes them.

For a new model primitive, document at minimum:

- semantic purpose;
- inputs/outputs and stateflow;
- parameter/state ownership and sharing rules;
- composition rules;
- static vs dynamic aspects;
- identity/serialization implications;
- learning-addressability implications;
- execution requirements that must be declared without being owned here;
- failure/validation conditions;
- at least one reference construction that needs it.

## Implementation posture

The initial repository is deliberately documentation-first. Do not infer from the absence of code that the first task is to create a large Rust/Python/C++ ML framework.

A healthy first implementation should be the smallest executable slice that proves the canonical model representation against real MNCS-language/runtime capability. Host code should remain generic backend/bootstrap machinery, not application-specific semantic policy.

When native MNCS implementation reaches or surpasses a host scaffold, deprecate and remove the scaffold from the canonical path rather than keeping two competing implementations alive.

## Verification

No executable conformance command is declared by this scaffold because no implementation has been selected yet. The first implementation campaign should establish:

- structural validation tests;
- deterministic identity/serialization tests where applicable;
- composition tests;
- parameter-sharing tests;
- recurrence/routing tests;
- at least one heterogeneous model-stack test;
- MNCS Actions evidence for the repository's actual verified boundary.

Do not add a green badge whose declared evidence is broader than what the tests truly prove.
