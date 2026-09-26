# Integration

`mncs-models` is intentionally narrow. Its value comes from providing a precise model-construction contract that the rest of the MNCS family can use without duplicating ownership.

This document defines the expected direction of those interfaces.

## Family-level picture

```text
raw/external information
        |
        v
   mncs-ingest
        |
        v
 typed observations / evidence
        |
        +-------------------------------+
        |                               |
        v                               v
   mncs-models                      mncs-memory
 model structure                    memory semantics
        |                               |
        |<------ explicit interface ---->|
        |
        v
    execution/runtime
        |
        v
 model outputs / state observations
        |
        v
    mncs-learn
 governed adaptation proposals
        |
        +--> parameter/state change
        +--> routing change
        +--> topology transformation
        |
        v
 updated canonical model/state
        |
        v
     mncs-store

rights/provenance constrains and traces the flow
Commons supplies shared identities/types where appropriate
Fabric chooses placement
Actions/Test/Debug/Doctor/Forge verify and operate the system
```

The diagram is conceptual. It does not prescribe a single runtime pipeline.

## `mncs-language`, compiler, and runtime

### Models needs

`mncs-models` needs a native way to express and/or lower:

- typed model structures;
- nested compositions;
- stable identities;
- parameter/state declarations and references;
- explicit sharing/aliasing;
- bounded recurrence;
- conditional routing;
- deterministic construction/serialization where required;
- generic numeric/model operations needed by reference constructions;
- capability/effect declarations where model components depend on external systems.

### Models provides

- real model-domain pressure on the language;
- bounded reference constructions;
- model-specific semantic invariants;
- examples that exercise combinations of generic language/runtime capabilities.

### Boundary

Do not implement missing general language semantics permanently inside `mncs-models`. If the missing capability is broadly reusable, pressure the language/compiler/runtime owner.

Do not fabricate `.mncs` syntax to make documentation look native before the language actually supports it.

## `MNCS-Commons`

### Likely shared concerns

Models should reuse Commons for concepts that are genuinely family-wide, such as stable identities, artifact references, generic capability descriptors, canonical digests, or shared transport-neutral types when Commons already owns them.

### Boundary

Do not copy Commons types into a model-specific parallel universe merely to avoid a dependency. Conversely, do not push model-only concepts into Commons just to make them appear general.

## `mncs-learn`

`mncs-learn` and `mncs-models` are closely coupled but deliberately separate.

### Models owns

- the model graph being learned;
- parameter/state declarations;
- routable structures;
- topology and component identity;
- legal structural transformations and validation of the resulting model.

### Learn owns

- whether evidence permits a change;
- operator selection;
- adaptation proposals;
- evaluation/fitness;
- commit/reject/defer policy;
- plasticity;
- timing of fast adaptation, consolidation, and structural evolution.

### Required handshake

A learning proposal should eventually be able to address targets such as:

```text
model
submodel
component
parameter/state declaration
connection/relationship
router/gate state
a structural region/topology target
```

without depending on host-language object identity.

A topology-changing learning event should result in a new canonical model structure or structural revision through declared transformation semantics. `mncs-learn` decides whether the transformation commits; `mncs-models` defines and validates the structural result.

The two repositories must not each maintain their own incompatible model graph representation.

## `mncs-ingest`

### Ingest owns

- parsing/acquisition from external sources;
- normalization into typed observations/evidence;
- source-specific processing;
- relevant provenance/rights attachment at ingestion boundaries.

### Models owns

- typed model input interfaces;
- any model-level representation expectations required for composition.

### Boundary

A model should not contain custom file parsers, web scrapers, media decoders, or dataset loaders simply because it needs input data.

Where tokenization, encoding, feature extraction, or media conversion sits should be decided by actual semantics. If a step is itself a learned model, it may be represented as a submodel. If it is source ingestion/decoding, it probably belongs elsewhere.

## `mncs-memory`

### Memory owns

- memory ingestion/storage semantics;
- retrieval/query semantics;
- episodic/semantic/etc. memory behavior;
- consolidation/conflict/freshness behavior;
- memory-specific persistent state.

### Models owns

- the fact that a model depends on memory;
- the typed interface by which a model component consumes memory results or emits memory-related requests where needed;
- model components that transform memory results as part of the model computation.

### Boundary

A "memory layer" in a paper does not automatically mean `mncs-models` should reimplement the memory system. Distinguish learned recurrent state internal to a model from a persistent external memory service with independent semantics.

Some architectures may legitimately contain differentiable/internal memory state. That state belongs in the model when it is part of the model's computational definition. Persistent semantic/episodic memory behavior remains `mncs-memory` territory.

## `mncs-store`

### Store owns

- durable storage/retrieval;
- content addressing and artifact persistence as defined by its contracts;
- checkpoints/model-state blobs;
- large parameter artifacts;
- retention/location/storage policy.

### Models owns

- structural declarations of what parameter/state artifacts a model needs;
- model manifests that reference those artifacts through stable store/artifact contracts;
- structural identity independent from a particular checkpoint when possible.

### Boundary

Do not embed storage paths, database semantics, or object-store policy into the model ontology.

## `mncs-rights-provenance`

Model construction can have several distinct provenance sources:

- architecture/construction source;
- imported model structure;
- imported pretrained parameter state;
- training/learning evidence;
- transformations such as pruning, distillation, merge, split, or architecture search;
- machine-generated structural decisions.

### Models owns

- stable identities and construction relationships needed to attach lineage;
- preservation of relevant provenance references through structural composition/transformation.

### Rights/provenance owns

- what use is allowed;
- lineage semantics;
- rights evaluation;
- attribution obligations;
- provenance policy and validation.

Do not duplicate rights decisions inside model constructors.

## `mncs-fabric` and execution/worker systems

### Models may declare

- required operation/capability families;
- numeric precision constraints that are semantically meaningful;
- memory/resource envelopes when they are part of model feasibility contracts;
- concurrency/parallelism opportunities;
- state locality constraints when model semantics require them.

### Fabric/execution owns

- worker selection;
- CPU/GPU/accelerator placement;
- distributed partitioning;
- retry/recovery strategy;
- scheduling;
- resource admission and runtime availability.

A model should remain the same semantic model when moved between valid execution placements.

## `mncs-actions`

Actions should eventually verify the repository's declared conformance boundary.

A future model-specific evidence producer should report only what it actually proves, for example:

- model graph validates;
- deterministic structural identity test passes;
- parameter sharing semantics pass;
- recurrent construction semantics pass;
- routing construction semantics pass;
- selected reference constructions compile/execute through the declared backend(s).

Do not claim full MNCS conformance merely because a small model example executes.

## `mncs-test`

Test should eventually be able to express model-domain assertions through the common language/runtime testing machinery.

Useful test categories include:

- malformed graph rejection;
- type/shape compatibility;
- stable identity;
- nested component addressing;
- parameter sharing;
- stateflow;
- recurrence;
- routing and sparse activation;
- heterogeneous submodel composition;
- canonical reconstruction;
- backend-equivalence where applicable.

Avoid creating a second model-only test framework if `mncs-test` can express the needed behavior.

## `mncs-debug`

Debug should be able to map runtime failures back to canonical model identities.

Desired failure context includes:

- model/submodel/component identity;
- input/output/state port involved;
- route/iteration/expert context;
- parameter/state artifact identity where relevant;
- backend realization mapping;
- violated model invariant.

This is another reason not to hide topology inside opaque host objects.

## `mncs-doctor`

Doctor may eventually diagnose whether the environment can realize a model's declared requirements:

- required backend/capability unavailable;
- artifact missing/incompatible;
- unsupported numeric representation;
- external capability interface unavailable;
- compiler/runtime capability too old or incomplete.

Doctor diagnoses capability; it should not redefine model semantics.

## `mncs-forge`

Forge may orchestrate building model artifacts/realizations and apply resource policy, but canonical model construction semantics should stay in `mncs-models` and generic compiler/runtime semantics in their owning repositories.

## Reference studies and historical implementations

When an old implementation remains useful for comparison but is no longer canonical, preserve it outside the active product path—such as in `mncs-reference-studies` where appropriate—instead of keeping multiple half-supported model implementations alive here.

This is especially relevant as old MNEL experiments are retired.

## Cross-repository migration rule

During the current coordinated-development stage, breaking a model contract is acceptable when the new design is healthier **if affected MNCS consumers are migrated as part of the campaign**.

The default response to contract improvement is:

```text
improve canonical contract
        |
        v
update mncs-models
        |
        v
migrate known family consumers
        |
        v
remove superseded path
```

not:

```text
keep old contract forever
create v2 beside it
maintain both indefinitely
```

A compatibility layer should exist only when an actual external compatibility constraint justifies its cost.

## Immediate integration debt to inspect

The old MNEL name may still appear in docs/contracts in repositories such as `mncs-learn` or other family members. The first implementation campaign should locate those references and classify them:

- model construction references should migrate to `mncs-models`;
- genuinely obsolete MNEL references should be removed;
- historical/reference mentions may remain when clearly labeled;
- learning-mechanism responsibilities should be assigned to their actual current owner rather than blindly renamed.

Do not perform a mechanical repository-wide `MNEL -> mncs-models` substitution without understanding each semantic reference.
