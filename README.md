# mncs-models

<!-- MNCS:generated:begin -->
## Project entry

Canonical MNCS model construction and composition layer for machine-native ML/AI systems: models as explicit typed computational structures assembled from composable primitives.

Declared capabilities (declarations do not establish execution health):


Semantic sources and ownership: `.mncs/projections.json`.
<!-- MNCS:generated:end -->

Canonical MNCS model construction and composition layer for machine-native ML/AI systems.

> **Core thesis:** a model is an explicit, typed computational structure assembled from composable primitives. Named architectures are useful recipes and research references, not the ontology of the repository.

`mncs-models` replaces the model-construction role that previously lived inside `machine-native-experimental-learning`. The surrounding MNCS family now owns most of the machinery that used to make an all-in-one experimental-learning repository necessary. This repository can therefore stay focused on the models themselves: what components exist, how they connect, what state and parameters they declare, how computation is routed or repeated, and how larger heterogeneous model stacks are composed.

The repository is intentionally architecture-open. It must be able to represent compact classifiers, specialist ensembles, transformers, recurrent and looped-depth systems, state-space and recurrent sequence models, mixtures of experts, multimodal systems, graph-based models, generative models, and future architectures that do not yet have a stable name.

## What this repository owns

`mncs-models` owns the **structural definition and construction of models**.

That includes:

- canonical model graphs and model-stack composition;
- model components, ports, edges, dataflow, and stateflow;
- parameter declarations and parameter-sharing relationships;
- recurrent regions, loops, iterative depth, and adaptive computation structure;
- routers, gates, sparse activation, expert sets, and conditional computation;
- parallel specialist/classifier structures and aggregation;
- representation, mixing, transformation, normalization, and readout/head structure;
- multimodal and heterogeneous model composition;
- explicit interfaces to memory, retrieval, tools, or other external capabilities without taking ownership of those systems;
- model identity, structural manifests, topology digests, and reproducible construction inputs;
- reference constructions that demonstrate how known architecture families emerge from the common primitives;
- machine-native descriptions needed by learning, storage, execution, verification, and other MNCS systems.

The repository should eventually be able to answer questions such as:

- What is this model made of?
- How are its components connected?
- Which parameters or state are shared?
- Where does recurrence occur?
- Which paths are conditional or sparse?
- Which components can execute in parallel?
- Which inputs, outputs, state channels, and capability dependencies does the model expose?
- How can another MNCS subsystem address a precise part of the model for learning, storage, verification, or execution?

## What this repository does not own

Keep the boundary sharp. `mncs-models` is not a replacement for the rest of the MNCS ML stack.

- **`mncs-learn`** owns learning semantics, adaptation proposals, evaluation, commit/reject/defer decisions, plasticity, and evidence-governed state transition.
- **`mncs-ingest`** owns conversion of external/raw information into machine-native observations and evidence.
- **`mncs-memory`** owns memory behavior, persistence/retrieval semantics, and memory-specific reasoning contracts.
- **`mncs-store`** owns durable artifact/state storage, including model artifacts, parameters, checkpoints, and related content where applicable.
- **`mncs-rights-provenance`** owns rights and provenance policy/lineage.
- **`mncs-fabric`** and execution infrastructure own placement, scheduling, devices, distributed execution, and worker availability.
- **`mncs-actions`, `mncs-test`, `mncs-debug`, `mncs-doctor`, `mncs-forge`, and related tooling** own verification, diagnostics, orchestration, and family-level evidence rather than model semantics.
- Dataset management, experiment tracking, deployment, serving, UI, and general benchmark infrastructure do not belong here unless a model-level contract genuinely requires a small interface to them.

A model may *declare* dependencies on memory, retrieval, tools, accelerators, precision, or other capabilities. Declaring an interface is not the same as owning the subsystem behind that interface.

## Design principle: primitives first, architecture names second

Do not build the repository as a collection of isolated architecture silos such as:

```text
transformer/
mamba/
moe/
loop-transformer/
next-paper-name/
```

Those names are useful as reference constructions, but they should be expressed from a smaller set of reusable model concepts.

The conceptual vocabulary is expected to converge around structures such as:

```text
Model
 ├─ Interface
 ├─ Component
 ├─ Port
 ├─ Edge / Connection
 ├─ Representation
 ├─ Transform
 ├─ Mixer
 ├─ State
 ├─ Parameter Set
 ├─ Parameter Sharing
 ├─ Router / Gate
 ├─ Expert Set
 ├─ Recurrent Region / Loop
 ├─ Aggregator
 ├─ Readout / Head
 └─ Composition / Submodel
```

The final native vocabulary must be driven by actual implementation pressure and MNCS-language capability rather than by this provisional list.

Known architectures should then become reproducible constructions over the shared primitives. For example, a dense transformer, a sparse MoE transformer, a recurrent-depth transformer, and a state-space/expert hybrid should share the parts that are actually semantically shared instead of duplicating entire architecture hierarchies.

## Dynamic and heterogeneous computation are first-class

MNCS should not assume that a useful model is one homogeneous feed-forward tensor stack.

A model graph may contain:

- small specialist classifiers executing in parallel;
- learned routers selecting a subset of specialists;
- shared blocks reused for multiple recurrent-depth steps;
- attention and state-space components in the same sequence model;
- modality-specific paths that merge later;
- experts with different internal structures;
- memory-conditioned or retrieval-conditioned subgraphs;
- deterministic and learned components in one stack;
- components that operate at different timescales;
- dynamically selected computation bounded by explicit model contracts.

This is a core use case, not an edge case.

## Explicit state and identity

A model definition must distinguish structure from mutable learned state.

At minimum, the architecture should make it possible for other MNCS systems to identify:

1. the structural model graph;
2. parameter/state declarations;
3. parameter-sharing relationships;
4. externally stored parameter/state artifacts;
5. runtime-only/transient state;
6. addressable components and submodels;
7. construction inputs and dependencies;
8. a deterministic structural identity or digest when semantics permit it.

`mncs-models` describes these things. It should not become the storage engine for them.

## One evolving implementation

This project currently has no compatibility burden that justifies parallel frozen implementations.

**Build and improve one canonical implementation.** When the design changes, migrate the repository and its known MNCS consumers forward together. Do not create `v1`, `v2`, `legacy`, `next`, or parallel half-implementations simply to avoid updating current code.

Versioned compatibility layers are appropriate only when a real external compatibility requirement exists. A schema/revision identifier used for serialized artifacts is not permission to maintain multiple competing product architectures.

## Machine-native direction

The desired end state is native MNCS expression of model structure and the critical semantics required to construct, inspect, validate, address, and execute model graphs.

Until `mncs-language` can represent a concept correctly:

- use the smallest transport-neutral or host bootstrap needed to make the pressure concrete;
- label bootstrap artifacts as such;
- record the missing language/runtime capability;
- push useful general primitives into the appropriate MNCS repository;
- do not invent attractive `.mncs` syntax and present it as executable;
- do not let a temporary host-language model framework become the permanent product by accident.

## Research posture

This repository should continuously absorb useful advances in model architecture without chasing paper names for their own sake.

Active areas include, but are not limited to:

- compact and parallel specialist/classifier systems;
- sparse and conditional computation;
- mixtures of experts and learned routing;
- recurrent-depth and looped transformers;
- adaptive computation and early-exit structures;
- recurrent, state-space, and hybrid sequence models;
- multimodal and modality-specialized composition;
- retrieval- and memory-conditioned models;
- graph and relational models;
- diffusion, flow, autoregressive, energy-based, and other generative constructions;
- model composition, architecture search, and eventually machine-constructed model topologies.

New research should normally pressure the common primitive set before introducing a one-off architecture abstraction.

See [`docs/RESEARCH_DIRECTIONS.md`](docs/RESEARCH_DIRECTIONS.md).

## Repository map

```text
AGENTS.md
    contributor/agent invariants and entry procedure

README.md
    project orientation and repository boundary

ROADMAP.md
    ordered path from scaffold to native model construction

mncs-boundary.json
    machine-readable ownership and integration boundary

rfcs/0001-model-construction-and-composition.md
    initial normative architecture decision

docs/ARCHITECTURE.md
    provisional model graph and primitive taxonomy

docs/INTEGRATION.md
    contracts with the wider MNCS family

docs/RESEARCH_DIRECTIONS.md
    architecture research intake and evaluation discipline
```

There is intentionally no implementation scaffold yet. The first implementation agent should derive the concrete representation from the RFCs, current MNCS-language capabilities, and the contracts already established in the surrounding repositories rather than inheriting an arbitrary host framework from this initial commit.

## Definition of a healthy foundation

The project is progressing in the intended direction when:

- models are represented compositionally rather than as unrelated named architecture silos;
- recurrence, routing, parameter sharing, sparse activation, and heterogeneous submodels are first-class structural concepts;
- model structure can be addressed and identified independently from learned parameter values;
- `mncs-learn` can target model state/topology without owning model definitions;
- `mncs-store` can persist model artifacts without defining model semantics;
- memory can participate through explicit interfaces without being reimplemented here;
- execution backends can consume the same model contract without redefining it;
- new research architectures can usually be expressed by composing existing primitives or by adding a genuinely general missing primitive;
- native MNCS expression steadily replaces bootstrap host artifacts;
- there is one canonical implementation rather than artificial generations of frozen partial designs.

## Start here

Agents and contributors should read, in order:

1. [`AGENTS.md`](AGENTS.md)
2. [`rfcs/0001-model-construction-and-composition.md`](rfcs/0001-model-construction-and-composition.md)
3. [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
4. [`docs/INTEGRATION.md`](docs/INTEGRATION.md)
5. [`ROADMAP.md`](ROADMAP.md)
6. [`docs/RESEARCH_DIRECTIONS.md`](docs/RESEARCH_DIRECTIONS.md)

Then inspect the current heads and relevant RFCs/docs of the MNCS repositories this project depends on before writing implementation code.

## License

Apache-2.0.
