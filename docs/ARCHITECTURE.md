# Architecture

This document records the current structural model for `mncs-models`. It is intentionally more precise than a vision statement and less rigid than a finalized schema.

The implementation should refine this document as real MNCS-language/runtime pressure is discovered.

## Architectural center

The repository treats a model as an **addressable typed composition graph**.

That graph is semantic, not necessarily the literal execution representation used by every backend. A compiler may fuse nodes, schedule work differently, lower recurrence into loops, or specialize routes while preserving the model's observable semantics and the identity relationships needed by the rest of MNCS.

The architectural center is therefore not "a neural network class." It is a machine-readable model structure that other MNCS subsystems can inspect, address, learn against, persist, prove, compile, and debug.

## Conceptual layers

A useful separation is:

```text
Construction intent
    |
    v
Canonical model structure
    |
    +--> parameter/state declarations
    +--> external capability declarations
    +--> structural identity/manifest
    |
    v
Instantiation bindings
    |
    +--> parameter/state artifacts
    +--> runtime resources/capabilities
    |
    v
Backend realization
    |
    v
Execution
```

`mncs-models` primarily owns the **canonical model structure**, construction semantics, and the model-facing parts of construction/instantiation manifests.

It should not own artifact persistence or worker scheduling merely because those are needed to instantiate a model.

## Structural concepts

The following are provisional semantic concepts.

### Model

An externally addressable composition with declared inputs, outputs, component graph, state/parameter declarations, and dependencies.

A model may be a complete deployable reasoning model, a compact classifier, an encoder, a router, a specialist, a multimodal fusion stack, or another independently meaningful composition.

### Submodel

A nested model composition reused inside another model.

Submodels should retain stable identity/addressing relationships so that learning, storage, provenance, debugging, and tooling can refer to them without depending on host-language object addresses.

### Component

An addressable computational element.

A component is not necessarily one hardware kernel or one source-language function. It represents a semantically meaningful operation or nested structure at the model level.

Examples may eventually include transforms, mixers, state-transition components, routers, aggregators, normalization operations, readouts, or wrapped submodels.

### Port

A typed endpoint on a model/component used for value, state, or control flow.

Ports should make composition machine-checkable. The final representation may use general MNCS type information rather than inventing a model-only type system.

### Connection

A declared relationship between compatible ports.

A connection should be explicit enough that validation, provenance, graph inspection, lowering, and debugging do not need to reverse-engineer hidden host callbacks.

### Parameter declaration

A declaration that a component/submodel depends on learned or externally supplied parameter state.

The declaration should describe identity/layout requirements needed by the model contract while allowing the actual bytes/artifacts to live in `mncs-store` or another appropriate system.

### State declaration

A declaration of mutable or carried model state.

Useful distinctions may include:

- persistent learned state;
- recurrent/carried state;
- runtime/transient state;
- externally supplied state;
- cached realization state that is not part of model identity.

The exact categories should be driven by actual use cases and existing MNCS contracts.

### Sharing / aliasing

An explicit relationship in which multiple model locations refer to the same semantic parameter/state object.

Sharing is required for weight tying, recurrent-depth parameter reuse, common backbones, expert sharing, adapters, and other modern model patterns.

### Representation

A description of model-visible values sufficient for components to compose safely.

This may involve element type, rank/shape constraints, sequence/set/graph structure, symbolic dimensions, modality tags, or semantic type information. Avoid creating a second type system if `mncs-language` already owns the required concepts.

### Transform

A component that changes a representation locally or pointwise in a broad sense.

Examples could include affine/linear transformations, nonlinear transforms, projections, normalization-related transforms, or other bounded operations.

This category is conceptual; the implementation may discover a better generalized primitive.

### Mixer

A component that combines information across positions/items/features/components.

Attention, convolution, recurrence/state-space scans, graph message passing, pooling, and other mechanisms may share some higher-level mixing semantics while remaining different internally.

Do not force unlike algorithms into a fake universal primitive. The purpose of the category is to search for genuinely reusable contracts.

### Router / gate

A component or structural mechanism that controls which paths/components participate and possibly how their results are weighted.

Routing should support explicit bounds and typed candidate sets. Learning the router belongs to `mncs-learn`; describing the router and candidate paths belongs here.

### Expert set / specialist set

A collection of addressable candidate components or submodels available to a router or aggregator.

The set may be homogeneous or heterogeneous.

An expert set should not imply that every expert shares an optimizer, parameter layout, architecture family, or execution device.

### Recurrent region / loop

A region of computation that is repeated while preserving explicit stateflow and parameter-sharing semantics.

A recurrent region should make it possible to represent repeated computation without cloning the entire region into a static chain.

Possible controls include fixed bounds, externally supplied step counts, bounded adaptive halting, or other policies. The model layer should represent the structural contract; runtime control realization may be lowered elsewhere.

### Aggregator

A component that combines results from parallel or conditional paths.

Aggregation may be deterministic, weighted, learned, sparse, hierarchical, or architecture-specific. The common requirement is that the merge semantics be explicit rather than hidden in orchestration code.

### Readout / head

A component/submodel mapping internal representations to externally meaningful outputs.

Heads may be shared, specialized, multi-task, modality-specific, or conditionally selected.

### External capability interface

A typed model dependency on a subsystem not owned by this repository.

Examples include memory query interfaces, retrieval inputs, tool results, external codecs/tokenizers, or declared backend capabilities.

An external interface must not become an excuse to duplicate the subsystem's internal policy or state machine inside `mncs-models`.

## Structural identity

Other MNCS systems need stable references to model structures.

The architecture should move toward distinct concepts for:

```text
structural model identity
parameter/state layout identity
particular parameter/state artifact identity
runtime realization identity
```

These identities may be linked, but they answer different questions.

A structural identity should ideally be reproducible from canonical construction information. A checkpoint identity necessarily depends on learned artifact content. A runtime realization identity may include backend-specific compilation/placement state that should not redefine the canonical model.

Nested components also need stable addressing. A future representation might derive component identities from parent identity plus canonical local identity, but the correct strategy must align with existing MNCS identity semantics rather than being invented locally.

## Static and dynamic structure

The repository must support both static structure and bounded dynamic computation.

Static graph concepts include:

- declared components;
- fixed connections;
- parameter sharing;
- known submodel composition.

Dynamic structure includes:

- route selection;
- sparse expert activation;
- optional modality paths;
- adaptive halting;
- repeated/recurrent regions;
- machine-selected subgraphs within declared constraints.

Dynamic computation should still be explicit enough to validate bounds, dependencies, addressability, and provenance. "Dynamic" must not mean "arbitrary host callback with invisible semantics."

## Model construction versus model transformation

Construction creates a canonical structure from declared primitives and inputs.

Transformation changes one canonical structure into another.

Examples of transformations include:

- adding/removing experts;
- splitting a model into specialists;
- merging submodels;
- changing depth or recurrent bounds;
- replacing a mixer;
- pruning paths;
- adding an adapter;
- changing shared/private parameter relationships.

`mncs-models` should own the structural operations required to represent/validate the resulting graph. When evidence decides that a transformation should occur, the proposal/evaluation/commit policy belongs to `mncs-learn`.

This separation is important: model transformation primitives can be structural without becoming learning policy.

## Architecture recipes

Known architecture families should be encoded as reference recipes/constructions after the base model vocabulary is executable.

Candidate references include:

### Compact classifier

Proves simple transforms, parameters, readout, and typed interfaces.

### Parallel specialist ensemble

Adds independent submodels, parallel paths, routing/aggregation, and possibly shared representations.

### Dense transformer-like block

Pressures sequence mixing, transform, normalization/residual paths, block composition, and heads.

### Recurrent-depth/looped transformer-like model

Pressures recurrent regions, shared parameters, carried state, bounded/adaptive iteration, and repeated-block addressing.

### State-space/recurrent sequence model

Pressures carried state and non-attention sequence mixing.

### Sparse expert model

Pressures routers, expert sets, bounded sparse activation, expert identity, and aggregation.

### Heterogeneous expert stack

Proves that experts need not share one architecture family.

### Multimodal composition

Pressures independent typed paths, shared/private parameters, fusion, optional paths, and modality-specific readouts.

These references should stay small enough to illuminate the common model contract rather than turning into production-scale replicas of external frameworks.

## What should remain backend-specific

The canonical model should avoid owning details that are purely realization choices, such as:

- exact CUDA kernel selection;
- memory allocator strategy;
- worker placement;
- graph partitioning across machines;
- operation fusion plans;
- kernel launch dimensions;
- backend-specific cache formats;
- quantized kernel implementation details when quantization does not alter declared model semantics;
- compilation artifacts.

Where such choices affect observable semantics, precision guarantees, capability requirements, or reproducibility, the canonical model may need to declare constraints without owning the backend implementation.

## Initial implementation pressure checklist

Before selecting concrete structures, inspect whether current MNCS already supports:

- stable semantic identities;
- records/variants/tagged unions;
- recursive/nested data;
- generic typed collections;
- symbolic dimensions or suitable shape contracts;
- deterministic canonical serialization/digests;
- graph-like references;
- callable/component references;
- bounded loops/recurrence;
- conditional dispatch/routing;
- explicit mutable state;
- artifact/content references;
- capability descriptors;
- effect/capability boundaries;
- generic numeric/tensor operations;
- backend realization metadata.

Every missing item should become a concrete pressure finding, not an assumption that `mncs-models` must implement it privately.

## Architectural smell tests

Reconsider a change if:

- adding a paper requires a new top-level framework rather than a small primitive;
- a model can only be understood by running host code;
- model topology is hidden inside callbacks/closures;
- a shared parameter is represented by copied values rather than shared identity;
- recurrence is represented only by duplicating layers;
- routing is embedded in orchestration code outside the model structure;
- learned weights must live in the same file/object as the topology;
- storage locations become model semantics;
- device placement becomes topology;
- memory implementation details appear in model components;
- learning policy appears in constructors;
- a language limitation creates a growing permanent host shadow rather than a tracked pressure;
- a redesign produces a second implementation tree instead of migrating the canonical path.
