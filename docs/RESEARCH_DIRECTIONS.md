# Research directions

`mncs-models` should remain open to new architecture research without becoming a museum of paper-specific classes.

The purpose of architecture research here is to answer:

> What new model semantics are useful enough to become reusable MNCS primitives, constraints, transformations, or reference constructions?

The purpose is **not** to maximize the number of named architectures represented in the repository.

## Research intake process

For each candidate architecture/mechanism:

1. **Identify the claimed capability.** What can this architecture do structurally that matters to MNCS?
2. **Separate architecture from training recipe.** Optimizer, loss, dataset, curriculum, augmentation, and benchmark details usually belong elsewhere.
3. **Separate semantics from implementation optimization.** Kernel fusion, CUDA tricks, quantization kernels, and memory layouts may matter to execution but are not automatically model primitives.
4. **Map the design onto existing model concepts.** Determine whether it is already expressible through composition, routing, recurrence, stateflow, sharing, aggregation, or existing transforms/mixers.
5. **Isolate the smallest missing primitive.** If the architecture cannot be represented cleanly, identify the general semantic gap.
6. **Look for a second use.** A proposed core primitive should normally help more than one named architecture or represent a broadly meaningful structural concept.
7. **Check family ownership.** Determine whether the missing capability actually belongs in models, language/runtime, learn, memory, ingest, store, Fabric, or another repository.
8. **Build a bounded reference construction.** Prove expressiveness with the smallest meaningful example before attempting a production-scale reproduction.
9. **Compare against a simpler baseline.** Do not keep structural complexity solely because a paper uses it.
10. **Record outcome.** Research should end in a reusable primitive, pressure finding, reference construction, integration issue, or explicit decision not to adopt the idea.

## Evaluation dimensions

A model idea is interesting to MNCS when it improves one or more of these dimensions:

- **composability** — combines cleanly with other model structures;
- **conditionality** — activates only useful computation;
- **parallelism** — exposes independent work without hiding semantics;
- **recurrence/iteration** — reuses computation or refines state over time/depth;
- **parameter efficiency** — shares or specializes parameters effectively;
- **state efficiency** — represents useful persistent/recurrent state compactly;
- **heterogeneity** — allows different model families to cooperate;
- **modality specialization** — preserves modality-specific structure while enabling fusion;
- **continual adaptability** — exposes structures that learning can update without rebuilding everything;
- **resource awareness** — allows bounded compute/memory behavior without hard-wiring placement;
- **interpretability/inspectability** — exposes meaningful addressable components/routes/state;
- **portability** — can be represented independently from one host framework/backend;
- **reproducibility** — construction is explicit enough to replay and identify;
- **machine constructability** — the architecture can eventually be assembled/transformed by MNCS itself.

Raw benchmark performance is evidence, but it is not the only architectural criterion.

## Active research families

The following families are deliberately broad. They are watch areas, not promises that every technique belongs in the canonical implementation.

### Compact classifiers and specialists

This continues the useful part of the original MNEL idea: many tasks may benefit from small specialized models rather than routing everything through one giant general model.

Questions:

- Can specialist models expose a common typed interface while remaining internally heterogeneous?
- When should specialists share a representation/backbone versus remain independent?
- How should specialist confidence/capability be represented without making evaluation policy part of the model?
- How can large numbers of small models be composed and addressed efficiently?
- Can specialists be created/split/merged by governed learning later?

Likely pressure areas: submodels, typed interfaces, parallel paths, parameter sharing, routing, aggregation, structural identity.

### Parallel classifier/router structures

Parallel classification or gating can cheaply narrow a problem before invoking expensive computation.

Questions:

- How are multiple classifier results combined?
- Can classifiers execute concurrently and feed a bounded router?
- How is uncertainty represented at the interface without imposing one statistical model?
- Can a route select one, several, or no downstream specialists?
- How do hard constraints interact with learned routing?

Likely pressure areas: router/gate semantics, parallel branches, bounded selection, fallback, aggregation, learning-addressable routing state.

### Mixtures of experts and sparse conditional computation

MoE is a special case of a broader requirement: only part of the available model graph may activate for a given input.

Questions:

- Are experts homogeneous or heterogeneous?
- How are capacity and selection bounds declared?
- How are shared and private expert parameters represented?
- How do nested routers compose?
- How are failed/unavailable experts distinguished from valid no-route decisions at runtime?
- Can routing change without redefining the expert structures?

Likely pressure areas: expert sets, routers, sparse activation, aggregation, capability matching, identities.

### Looped and recurrent-depth transformers

These models reuse blocks across depth/iterations rather than treating depth only as a static stack of separately parameterized layers.

Questions:

- How should recurrent-depth state be represented?
- What is structurally identical across iterations?
- How should adaptive halting be bounded?
- How do we inspect or debug a particular iteration while preserving one shared block identity?
- Can recurrence be nested with expert routing or multimodal paths?

Likely pressure areas: recurrent regions, parameter sharing, carried state, iteration identity, bounded dynamic computation, halting/continuation.

### Adaptive computation and early exit

Models may spend different amounts of computation on different inputs.

Questions:

- How are optional additional computation steps represented?
- What is the boundary between model-declared possible paths and runtime scheduling?
- How do we enforce maximum work?
- How are intermediate readouts represented?
- Can learning change halting state/policy without changing the model ontology?

Likely pressure areas: bounded loops, routing, readouts, dynamic control, resource declarations.

### Recurrent and state-space sequence models

Attention is not the only useful sequence mechanism. Recurrent/state-space structures may provide different scaling and state behavior.

Questions:

- What is the minimum common interface between attention, recurrence, scans, and state-space mixing?
- Which state is persistent across tokens/steps versus ephemeral within one invocation?
- How are parallel training forms related to sequential inference semantics without importing training machinery into the model definition?
- How should selective/gated state updates be represented?

Likely pressure areas: stateflow, mixer abstraction, recurrence, scan-like structure, backend lowering.

### Hybrid sequence models

Architectures increasingly mix attention, convolution, recurrence, state-space computation, and experts.

Questions:

- Can different mixer families be swapped/composed under a common outer block contract?
- What semantics genuinely belong in a shared interface?
- Which differences should remain component-specific rather than forced into a universal abstraction?

Likely pressure areas: nested composition, typed representations, reusable component interfaces.

### Multimodal models

Multimodal architectures often need both specialized modality paths and shared latent computation.

Questions:

- How are modalities typed without freezing a closed modality enum forever?
- How are independent encoders/decoders composed?
- How are shared/private backbones and heads represented?
- How do optional/missing modalities affect routing?
- When is a tokenizer/codec part of the model versus ingest/media infrastructure?

Likely pressure areas: typed interfaces, submodels, shared/private parameters, routing, fusion/mixing, external capability boundaries.

### Graph and relational models

Graph neural networks and relational models pressure structures that are not naturally sequence-first.

Questions:

- Does general MNCS typed data already describe graph inputs sufficiently?
- How should message passing/mixing be represented without making graph-specific topology collide with model graph topology?
- Can graph neighborhoods be dynamic while the model structure remains stable?

Likely pressure areas: representation semantics, mixer interfaces, dynamic data structure versus static model structure.

### Memory- and retrieval-conditioned models

Models increasingly consume external retrieved context or memory state.

Questions:

- What is the explicit model interface to retrieval/memory?
- Which cache/recurrent state is internal model state versus external memory?
- How can a model request/use memory without owning memory policy?
- How are retrieved items typed and provenance-preserving?

Likely pressure areas: external capability interfaces, typed context ports, state boundaries, provenance hooks.

### Generative architecture families

The model layer should not assume all generation is autoregressive next-token prediction.

Research areas include:

- autoregressive models;
- diffusion/denoising models;
- flow/flow-matching constructions;
- masked/iterative refinement;
- energy-based models;
- latent-variable models;
- discrete and continuous generative processes.

Questions:

- Which iterative process semantics are shared?
- What state/time/noise/schedule concepts are model structure versus learning/inference configuration?
- Can iterative generators reuse the same recurrence primitives as other model families?

Likely pressure areas: iterative/recurrent regions, state, conditioning interfaces, time/step representation, readouts.

### Continuous-time and neural differential models

Continuous-time models may become useful for physical systems, control, irregular time series, and simulation-adjacent tasks.

Questions:

- Does the model need explicit differential/integration semantics or merely a component interface to a general numeric subsystem?
- What solver choices are semantic versus backend realization details?
- How are tolerances/bounds represented when they affect semantics?

Likely pressure areas: external numeric capabilities, state transition components, semantic constraints versus realization choices.

### Modular world models and predictive systems

World-model systems may combine encoders, dynamics models, latent state, planners/controllers, and specialized predictors.

Questions:

- Can these be represented as ordinary nested model stacks rather than a new world-model ontology?
- Where do memory/state and model-state boundaries sit?
- Which planning components are models versus agents/actions/tooling?

Likely pressure areas: heterogeneous submodels, stateflow, external capability interfaces, composition.

### Architecture search and machine-constructed models

Long-term, MNCS should be able to build model structures using the same primitives humans use.

Questions:

- What structural transformations are legal?
- How are resource/type/capability constraints expressed?
- How can candidate architectures be compared without embedding evaluation policy here?
- How are machine-generated structural decisions provenance-tracked?
- Can `mncs-learn` propose architecture changes that `mncs-models` validates and constructs?

Likely pressure areas: model transformations, canonical construction manifests, structural identity, constraints, learn integration.

## Research source discipline

Architecture work should prefer primary sources and executable evidence:

1. original papers/preprints;
2. official project/model repositories;
3. reproducible implementations and technical reports;
4. independent replications or strong comparative studies when available.

Blog posts and summaries are useful for discovery but should not be the sole basis for a canonical architectural decision.

When an idea is new or weakly replicated, label that uncertainty. The repository should be able to experiment without pretending every promising result is established.

## External code discipline

Do not copy large external model frameworks into `mncs-models` as a shortcut.

Reference implementations may be studied or used as backends where licensing and architecture allow, but canonical MNCS semantics should be independently represented through the repository's model contract.

Preserve provenance and licensing information for imported architecture knowledge, pretrained artifacts, or adapted code through the appropriate MNCS rights/provenance processes.

## When to add a new primitive

A new primitive is justified when most of the following are true:

- existing primitives cannot express the semantics without hidden behavior;
- the missing concept affects construction/validation, not merely optimization;
- the concept is useful beyond one exact paper implementation;
- its ownership clearly belongs in model structure rather than another MNCS subsystem;
- it can be given explicit type/state/composition semantics;
- it improves inspectability or avoids duplicated special cases;
- at least one bounded reference construction demonstrates the need.

A new primitive is probably **not** justified when:

- it is only a training trick;
- it is only a kernel optimization;
- it can be expressed cleanly by composing existing components;
- it exists only to preserve the vocabulary of one paper;
- its semantics are actually owned by memory, learning, ingest, storage, Fabric, or rights/provenance;
- it would require a parallel host runtime with no path toward native MNCS representation.

## Research output template

When an agent investigates a model advance, record the result in roughly this form:

```text
Candidate:
Source(s):
Claimed capability:
Architecture semantics:
Training-only details:
Backend-only details:
Existing mncs-models primitives that cover it:
Missing primitive(s), if any:
Other MNCS repository pressures:
Reference construction worth adding:
Evidence/replication confidence:
Decision:
```

This keeps research connected to architecture rather than turning the repository into a reading list.
