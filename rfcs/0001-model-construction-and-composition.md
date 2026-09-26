# RFC 0001 — Machine-native model construction and composition

Status: Accepted as the initial repository charter

## Summary

`mncs-models` defines the canonical structural representation and construction semantics for ML/AI models in the MNCS ecosystem.

The repository adopts a composition-first model:

> A model is an explicit, typed computational structure assembled from reusable primitives. Architecture names describe reproducible constructions over those primitives; they do not define isolated top-level ontologies.

The repository supersedes the model-construction portion of `machine-native-experimental-learning` while deliberately leaving learning, ingestion, memory, storage, provenance, execution placement, and orchestration in their existing owning repositories.

## Motivation

The original experimental-learning direction was valuable because it treated small specialists, classifiers, routers, and heterogeneous computational structures as useful building blocks rather than assuming that every intelligent system must be one large homogeneous network.

As the MNCS family has expanded, however, most of the machinery needed around models now has explicit homes:

- ingestion has its own boundary;
- learning has its own evidence-governed lifecycle;
- memory has its own semantics;
- storage can own durable artifacts and checkpoints;
- rights/provenance has its own lineage and policy layer;
- fabric/execution infrastructure can own placement;
- language/compiler/runtime work can own general executable semantics;
- Actions/Test/Debug/Doctor/Forge can own verification and development machinery.

Keeping model construction inside a broad experimental-learning repository would therefore duplicate responsibility and make architectural work harder to reason about.

At the same time, modern model research increasingly combines architectural mechanisms rather than respecting clean family boundaries. Attention may be mixed with recurrence or state-space computation. Expert routing may operate inside multimodal systems. Parameter-shared looped depth may reuse the same block multiple times. Small specialist models may run in parallel and feed a larger integrator. New architectures will continue to combine old ideas in new ways.

A repository organized primarily around architecture names would accumulate duplicated, incompatible abstractions.

## Decision

### 1. The repository owns model structure, not the entire ML lifecycle

`mncs-models` owns the canonical representation and construction of model graphs and model stacks.

It owns structural concepts including:

- model and submodel composition;
- typed interfaces, ports, and connections;
- component identity;
- parameter and state declarations;
- parameter/state sharing;
- recurrent regions and loops;
- conditional routing and sparse activation;
- expert/specialist composition;
- aggregation and readout structure;
- multimodal and heterogeneous paths;
- construction manifests and structural identity;
- reference architecture constructions.

It does not own training/learning policy, data ingestion, memory semantics, durable storage, rights/provenance policy, worker placement, serving, deployment, or experiment orchestration.

### 2. The canonical abstraction is a typed computational graph

The initial conceptual model is a graph of addressable components connected through typed interfaces.

This does **not** require every backend to execute a literal graph interpreter. The graph is a semantic representation. Compilers and backends may lower, fuse, schedule, specialize, or otherwise realize it as long as observable model semantics and identity mappings required by the wider system are preserved.

A useful model representation should be able to describe, at minimum:

- external model inputs and outputs;
- nested components/submodels;
- connections/dataflow;
- persistent and transient stateflow;
- parameter declarations;
- shared/aliased parameters;
- repeated/recurrent computation;
- conditional routes;
- aggregation/readout;
- explicit external capability dependencies.

### 3. Architecture families are reference constructions

Known architectures should normally be represented as constructors/recipes over common primitives rather than as isolated implementation universes.

A dense transformer may use sequence mixing, transforms, normalization, residual paths, and readouts.

A sparse expert transformer should reuse those same semantics plus routing/expert-set concepts.

A recurrent-depth transformer should reuse the same block while introducing explicit recurrence/iteration and shared parameters rather than copying the block into a deeper static stack.

A state-space/expert hybrid should combine state transition/mixing structures with the same expert/routing primitives.

The purpose of reference constructions is to:

- prove the primitive vocabulary is expressive enough;
- provide known-good examples;
- compare semantics across families;
- pressure missing primitives;
- provide material for tests and benchmarks owned by the appropriate systems.

Reference constructions are not permission to make paper-specific abstractions normative without evidence.

### 4. Structure and learned state are separate concepts

The canonical model definition must not depend on embedding learned parameter bytes directly into topology.

A model definition should be able to identify parameter/state declarations and refer to their artifacts without becoming the storage system.

This separation is required so that:

- the same structure can be instantiated with different learned states;
- `mncs-learn` can target precise parameter/state/topology locations;
- `mncs-store` can persist and retrieve artifacts independently;
- model structure can have a stable identity distinct from a particular checkpoint;
- provenance can track construction lineage and learned-state lineage separately.

Some state is structural, some persistent and learned, and some runtime/transient. The representation must be able to distinguish these categories where they affect semantics.

### 5. Parameter sharing is explicit

Parameter sharing must not be inferred from duplicated names or hidden host references.

The model layer must eventually support explicit relationships such as:

- tied input/output embeddings;
- recurrent blocks sharing one parameter set across iterations;
- experts sharing selected parameter subsets;
- modality paths sharing a backbone but retaining private heads;
- adapters or low-rank structures referencing base parameters;
- submodels intentionally reusing the same state declaration.

A shared parameter is one semantic object referenced from multiple locations, not merely equal bytes copied to several locations.

### 6. Recurrence and repeated computation are explicit

Looped or recurrent computation must not be defined solely by materializing N copies of the same component.

The canonical model should be able to express:

- recurrent regions;
- iteration bounds or policies;
- state carried between iterations;
- shared parameter sets;
- halting/continuation interfaces;
- inspection/addressing of repeated computation where needed;
- nested recurrence subject to explicit validation.

This supports recurrent neural networks, recurrent-depth transformers, adaptive compute, iterative refiners, and future loop-based architectures without architecture-specific special cases.

### 7. Routing and sparse/conditional computation are explicit

The model graph may contain paths that are selected conditionally rather than all being active for every input.

The representation should support the structural semantics needed for:

- learned routers/gates;
- bounded top-k or subset selection;
- expert selection;
- early exit;
- branch selection;
- optional modality paths;
- sparse activation;
- fallback/no-route behavior;
- aggregation after conditional paths.

The model describes the available routes and relevant state. `mncs-learn` owns governed changes to learned routing state. Execution systems own placement and scheduling.

### 8. Heterogeneous model stacks are valid

A model stack is not required to be one architecture family.

It may contain, for example:

```text
input
  |
  v
router
  |--------------------|---------------------|
  v                    v                     v
small classifier   recurrent reasoner   state-space specialist
  |                    |                     |
  |--------------------|---------------------|
                       v
                   aggregator
                       |
                       v
                    readout
```

The components may have different internal structures as long as their typed interfaces compose.

This preserves the useful micro-model theme from MNEL without making "micro-model" a restrictive ontology of its own.

### 9. External capabilities are declared through interfaces

Models may depend on systems outside the model graph, including memory, retrieval, tools, encoders/decoders, or hardware capabilities.

The model may declare such an interface or requirement. It must not absorb the owning system's semantics merely to make the declaration convenient.

For example:

- a memory-conditioned model may declare a memory query/read interface;
- a retrieval-conditioned model may declare retrieval inputs;
- a model realization may declare accelerator or precision requirements;
- a multimodal model may declare an external tokenizer/codec boundary where appropriate.

The owner of each capability remains responsible for its semantics.

### 10. Structural identity should be deterministic where possible

MNCS systems need to address and compare model structures across learning, storage, debugging, provenance, and execution.

The model layer should therefore move toward deterministic structural manifests and identities derived from canonical construction information where semantics permit it.

Identity should distinguish at least conceptually:

- model structure/topology;
- parameter/state declaration layout;
- particular learned parameter/state artifacts;
- runtime realization/backend instance.

These may be related but should not be collapsed into one identifier.

### 11. The native target is MNCS, not a permanent host framework

The canonical semantics should move toward native `mncs-language` expression as capabilities become available.

A bootstrap schema or host implementation is acceptable only when it makes progress measurable or exposes a concrete missing native capability.

Bootstrap code must not quietly become a second semantic authority.

If MNCS-language cannot express a required model concept, the preferred response is to identify the smallest general pressure and improve the owning language/runtime layer rather than building a large private workaround in `mncs-models`.

### 12. Maintain one evolving canonical implementation

The project currently operates under coordinated control of the relevant MNCS repositories. Compatibility can usually be restored by migrating consumers together.

Therefore, this repository will not use artificial `v1`, `v2`, `legacy`, `next`, or similar implementation trees as the normal development strategy.

When the canonical design improves:

1. update the canonical contract;
2. migrate the implementation;
3. migrate known consumers;
4. remove superseded scaffolding when replacement capability reaches or exceeds it;
5. preserve old material only when it has real reference value, ideally outside the canonical product path.

This decision does not prohibit explicit revisions in serialized artifact formats when compatibility actually requires them.

## Provisional primitive taxonomy

The following vocabulary is a research scaffold, not a frozen schema:

- **Model** — a complete externally addressable composition.
- **Submodel** — a nested composition that may also be independently reusable.
- **Component** — an addressable computational element.
- **Port** — a typed input/output/state endpoint.
- **Connection** — a typed relationship carrying values/state between ports.
- **Representation** — declaration of model-visible value structure/shape/domain as required.
- **Transform** — point/local transformation of a representation.
- **Mixer** — combines information across positions/items/features/components.
- **State** — declared mutable or carried information.
- **Parameter set** — learned or externally supplied parameter declarations.
- **Alias/share** — explicit multiple references to one parameter/state object.
- **Router/gate** — chooses or weights paths/components.
- **Expert set** — a collection of candidate submodels/components addressable through routing.
- **Recurrent region** — explicitly repeated computation with carried state and/or shared parameters.
- **Aggregator** — combines multiple paths/results.
- **Readout/head** — maps internal representation to an externally meaningful output.
- **External capability interface** — typed dependency on a subsystem not owned by the model.

Implementation work may rename, merge, split, or remove these concepts as real pressure clarifies the correct abstraction.

## Validation requirements

The eventual canonical representation should reject at least:

- dangling or unresolvable component/port references;
- incompatible typed connections;
- invalid parameter/state aliases;
- ambiguous ownership of state;
- unbounded dynamic structures where the runtime contract requires explicit bounds;
- impossible route/aggregation combinations;
- identity collisions created by non-canonical construction data;
- nested/submodel cycles that are not explicitly represented as legal recurrence;
- undeclared external capability dependencies.

Backend-specific shape/device constraints may add stricter validation without redefining model semantics.

## Integration consequences

### `mncs-learn`

Learning must be able to address model state, parameters, routing structures, and topology through stable model identities. Topology-changing learning should produce a replacement canonical structure/manifest rather than mutate hidden host objects.

### `mncs-store`

Store should persist/retrieve model definitions and referenced parameter/state artifacts. Storage location/content addressing must not become hard-coded into model semantics.

### `mncs-memory`

Memory-conditioned models should depend on explicit memory interfaces. Memory indexing, retrieval, consolidation, conflict handling, and persistence remain memory concerns.

### `mncs-ingest`

Ingest should provide typed observations/evidence that can bind to model interfaces without forcing model-specific raw parsing into this repository.

### rights/provenance

Construction sources, imported model artifacts, learned state, and machine-generated topology changes should remain traceable. The model layer should carry stable hooks/identities, while policy and lineage semantics remain owned by rights/provenance systems.

### compiler/runtime/fabric

Compilers and runtimes may lower/fuse/schedule the model graph. Fabric may decide placement. Those choices should not require rewriting the semantic model definition unless they change the model itself.

## Alternatives considered

### Keep machine-native-experimental-learning as the umbrella

Rejected. The MNCS family now has explicit owners for most surrounding machinery, making an umbrella repository redundant and likely to duplicate responsibilities.

### Organize by architecture family

Rejected as the primary ontology. It encourages duplicate concepts and makes hybrid architectures awkward. Architecture-specific reference constructions remain useful.

### Make `mncs-learn` own models

Rejected. Learning describes how evidence governs change; model construction describes the computational object being changed. Keeping them separate allows the same model to participate in different learning processes and allows non-learning inference/static models to exist cleanly.

### Use an existing host ML framework as the canonical representation

Rejected. Host frameworks may provide useful backend/reference execution, but their object model would become an accidental semantic authority and constrain machine-native composition.

### Encode every research architecture directly as MNCS syntax immediately

Rejected. Unsupported or guessed syntax produces documentation theater rather than pressure-driven language development. Native representation should follow verified language/runtime capability.

## Open questions

The first implementation phases must resolve these empirically:

- What exact type/shape vocabulary belongs in the model layer versus general MNCS types?
- Which graph/composition primitives already exist in `mncs-language`/Commons?
- How should deterministic nested component identities be derived?
- How should structural model identity relate to parameter-layout identity and checkpoint identity?
- What is the cleanest representation of bounded dynamic routing and adaptive-depth control?
- Which state distinctions belong in the model contract versus runtime execution metadata?
- How should model construction reference external codecs/tokenizers/embedders without absorbing ingest/media responsibilities?
- Which backend requirements are semantic constraints versus placement hints?
- What model graph transformations should be canonical operations versus learning proposals owned by `mncs-learn`?

These questions are deliberate implementation pressure, not reasons to invent parallel speculative designs.
