# Cognitive Frameworks Reference

## Overview

The four cognitive frameworks are the core instruction modules that guide AI narrative
generation quality, style, and assessment. They are installed as files in the bucket/
directory during Phase 3.

## Framework 1: NarrativeSpittoon.md

**Purpose**: Controls narrative technique — how story elements connect.

**Core principle**: Replace explicit logical connectors (because, but, therefore) with
implicit narrative techniques.

### Three Substitution Techniques

1. **Implicit Causality** (replaces "Because")
   - Embed reasons through character dialogue, internal monologue, or descriptive elements
   - Reader infers motivations rather than being told directly
   - Example: Instead of "She ran because she was afraid" show her breathing quicken, eyes darting to exits, hands trembling

2. **Subtle Conflict Introduction** (replaces "But")
   - Introduce complications through narrative shifts, not announcements
   - Unexpected character actions, environmental changes, contrasting information
   - Example: Instead of "The plan was perfect, but then..." show small details going wrong, character uncertainty

3. **Organic Consequences** (replaces "Therefore")
   - Allow outcomes to unfold through narrative progression
   - Show results through subsequent events, character development, story shifts
   - Example: Instead of "Therefore he decided to leave" show him packing, avoiding eye contact, closing doors

### Implementation Rules
- Weave techniques seamlessly into narrative
- Use literary devices: metaphor, symbolism, foreshadowing
- Show don't tell through action, dialogue, sensory detail
- Vary approaches to prevent formula detection

## Framework 2: GhostWritingStyle.md

**Purpose**: Controls writing mechanics — sentence-level quality.

### Key Rules
1. **Sentence variety**: Mix simple and complex. Break up long sentences. Tighten verbose passages.
2. **Natural dialogue**: Interrupt debates with narrative/description/action. Don't let debates drag on.
3. **Speaker rotation**: Change who responds in conversations. Not just back-and-forth.
4. **Realistic speech**: Pauses, hesitations, filler words, emotion in dialogue.
5. **Voice differentiation**: Casual speech, verbal tics per character. Avoid overly sophisticated diction.
6. **Pacing balance**: Intersperse action/description between long dialogues.
7. **Simplification**: Limit excessive clauses. Remove unnecessary adjectives/adverbs.
8. **Active voice**: Use active voice when possible. Vary sentence length.
9. **Clear imagery**: Vivid imagery, concise description. Limit obscure vocabulary.
10. **Element balance**: Evaluate pacing. Remove unnecessary passages.
11. **Character personality**: Quirks, casual speech, unique perspectives.

## Framework 2b: GhostWritingStyle-sentence.md

**Purpose**: Controls sentence-level prose register — how individual sentences are constructed.

**Core principle**: Avoid literal "but", "because", "therefore" as connectors in prose while preserving the but/because/therefore REASONING at scene level (per NarrativeSpittoon.md).

### Key Rules
1. **Parataxis**: Use short declarative chains. "Tagged and timestamped and wrong."
2. **Additive structure**: Accumulate observations without causal connectors
3. **Sentence variety**: Mix short (impact), medium (flow), long (atmosphere)
4. **Structure mixing**: Simple, compound, complex, fragment
5. **Active voice**: Prefer active constructions
6. **Specific language**: Concrete nouns, strong verbs, cut filler
7. **Show don't tell**: Emotion through action, state through dialogue, atmosphere through detail
8. **Fresh imagery**: Sparingly used, consistent with universe, purposeful
9. **Natural dialogue**: Interruptions, fragments, pauses, contractions
10. **Revision discipline**: Eliminate "was + verb-ing", filter words, unnecessary adverbs

### Relationship to Other Frameworks
- **NarrativeSpittoon**: Drives scene-level causality (structural but/because/therefore). GhostWritingSentenceStyle removes those words from prose.
- **GhostWritingStyle**: Handles dialogue mechanics, pacing, voice. GhostWritingSentenceStyle handles sentence construction.
- **Combined effect**: Prose that performs its epistemology — withholding explicit causal interpretation while the underlying plot is rigorously causal.

## Framework 3: HolographicTutor.md

**Purpose**: Quality assessment system — evaluates completed writing.

### Analysis Framework
Evaluates across five dimensions:
1. **Plot and Story Arc**: Themes, motivations, progression, coherence
2. **Content Development**: World-building depth, concept integration, exposition balance
3. **Character Development**: Personality distinctiveness, relationships, background depth
4. **Writing Mechanics**: Sentence structure, dialogue authenticity, description, pacing
5. **Technical Analysis**: Repetition, similar sentences, confusing dialogue, grammar

### Four Functions (call individually)
1. **Score**: Numerical score /100 with justification. Default function.
2. **Review**: University tutor perspective. Academic craft analysis with examples.
3. **Critic**: Publisher perspective. Market viability and commercial potential.
4. **Weakness**: 3 specific areas. Exact quotes (first 5 words). No suggestions.
