---
name: nsi4-workflow
description: >
  This skill should be used when the user asks about Narrative Spittoon Inversion,
  NSI workflow, reverse story generation, writing stories backwards, narrative bucket,
  LoreBook, cognitive frameworks for writing, HolographicTutor, GhostWritingStyle,
  NarrativeSpittoon framework, NSL format, reverse chronological narrative, or wants
  help planning, outlining, or generating a story using the NSI methodology. Also
  triggered by /nsi4-start, /nsi4-interview, /nsi4-bucket, /nsi4-frameworks,
  /nsi4-generate, /nsi4-refine, or /nsi4-export commands.
version: 4.0.0
tools: Read, Glob, Grep
---

# Narrative Spittoon Inversion 4.0 — Workflow Knowledge

## What is NSI?

Narrative Spittoon Inversion (NSI) is an AI-assisted story creation methodology that generates narratives in **reverse chronological order** — from the ending to the beginning. This approach creates tightly plotted stories where every scene naturally leads to the next, ensuring narrative coherence and purposeful character development.

## Core Principle: Writing in Reverse

Stories are written **backwards**: Page 5 (ending) → Page 4 → Page 3 → Page 2 → Page 1 → Page 0 (beginning).

Each page answers the question: **"What led to the next page's events?"**

### Why Reverse Works

- **Eliminates plot drift**: Starting from the ending prevents stories from wandering
- **Ensures causality**: Each scene is reverse-engineered from its outcome
- **Natural foreshadowing**: Earlier pages naturally set up later events
- **Character purpose**: Arcs are built from destination backward
- **Hero's Journey integration**: Classical structure applied in reverse creates natural progression

## The 5-Phase Workflow

### Phase 1: Knowledge Gathering (`/nsi4-interview`)
Create a comprehensive LoreBook through a 20-question dynamic interview covering universe, characters, plot, themes, tone, and the ending. The LoreBook becomes the foundation for all subsequent artifacts.

### Phase 2: Bucket Artifact Creation (`/nsi4-bucket`)
Distill the LoreBook into specialized artifacts:
- `world.md` — Setting, geography, history, culture, systems
- `characters.md` — Character profiles with personality, quirks, motivations, relationships
- `speechstyles.md` — Per-character speech patterns, vocabulary, verbal tics
- Technical specs (`.json`), diagrams (`.mermaid`), glossary (`.txt`)

### Phase 3: Core Framework Setup (`/nsi4-frameworks`)
Install three cognitive frameworks that guide AI generation quality:
1. **NarrativeSpittoon.md** — Implicit causality, subtle conflict, organic consequences (eliminates "because/but/therefore")
2. **GhostWritingStyle.md** — Sentence variation, natural dialogue, active voice, pacing
3. **HolographicTutor.md** — Quality assessment with Score/Review/Critic/Weakness functions

Generate `project-instructions.md` as a manifest indexing all bucket contents.

### Phase 4: Story Generation — The Inversion (`/nsi4-generate`)
Reverse-generate the story with approval gates between each page:
1. Create or approve Page 5 (the ending)
2. Generate Page 4 by asking "what led to Page 5?"
3. Pause for user approval
4. Continue backward through Page 0

Each page must:
- Reference all bucket files for consistency
- Apply NarrativeSpittoon framework (show, don't tell)
- Follow GhostWritingStyle rules
- Match Hero's Journey stage for that page number
- Flow naturally into the next page
- Target 800-1500 words

### Phase 5: Refinement (`/nsi4-refine`)
Optional polish passes (recommended order):
1. Quality Assessment (HolographicTutor Score)
2. Speech Style Pass (voice consistency)
3. Repetition Sniper (eliminate redundancy)
4. Narrative Smoothing (transitions and foreshadowing)
5. Environmental Enhancement (sensory depth)

For detailed refinement pass instructions, see: `references/refinement-passes.md`

For validation checklists and troubleshooting, see: `references/nsi4-process-guide.md`

## Hero's Journey in Reverse

| Page | Hero's Journey Stage (Reverse) | Story Function |
|------|-------------------------------|----------------|
| 5 | Return with Elixir / Resolution | Story conclusion, transformation complete |
| 4 | Resurrection / Climax | Final challenge, ultimate test |
| 3 | Road Back / Rising Action | Consequences unfold, stakes escalate |
| 2 | Ordeal / Commitment | Major challenge, point of no return |
| 1 | Tests, Allies, Enemies / Setup | World establishment, character introduction |
| 0 | Ordinary World / Opening | Story beginning, initial state |

For detailed per-page generation guidance and scaling, see: `references/heros-journey-mapping.md`

## The Narrative Bucket

A "narrative bucket" is the complete collection of artifacts that define a story project. It contains world-building, character profiles, speech styles, cognitive frameworks, technical specs, and the project manifest. All files live in the `bucket/` folder.

### Required Bucket Files
- `LoreBook.md` — Raw knowledge base (Phase 1)
- `world.md` — Distilled world-building
- `characters.md` — Character profiles
- `speechstyles.md` — Speech patterns
- `NarrativeSpittoon.md` — Narrative framework
- `GhostWritingStyle.md` — Writing style guide
- `HolographicTutor.md` — Quality assessment system
- `project-instructions.md` — Component manifest

### Optional Bucket Files
- `[name]-glossary.txt` — Universe terminology
- `*.json` — Technical specifications
- `*.mermaid` — Visualization diagrams

## Three Cognitive Frameworks

### NarrativeSpittoon (Narrative Quality)
Replaces explicit "because/but/therefore" with:
- **Implicit Causality**: Embed reasons through dialogue, monologue, description
- **Subtle Conflict**: Introduce complications through shifts, not announcements
- **Organic Consequences**: Let outcomes unfold through progression

### GhostWritingStyle (Writing Mechanics)
- Vary sentence structure and length
- Make dialogue flow naturally with interruptions
- Rotate speakers in conversations (not just back-and-forth)
- Inject pauses, hesitations, filler words
- Use casual speech and verbal tics for voice differentiation
- Simplify complex sentences, use active voice
- Balance pacing between elements

### HolographicTutor (Assessment System)
Four functions (call individually):
- **Score**: Numerical score out of 100 with justification
- **Review**: Comprehensive academic analysis with examples
- **Critic**: Publisher perspective with market viability
- **Weakness**: 3 specific areas needing improvement (quotes, no suggestions)

For detailed framework implementation rules and examples, see: `references/cognitive-frameworks.md`

## NSL 1.1 Format

The Narrative Spittoon Language (NSL) is an XML-based format that packages an entire narrative bucket into a single portable `.nsl` file. Use `/nsi4-export` to convert between bucket folders and NSL files.

For detailed NSL specification, see: `references/nsl-1.1-specification.md`

## Scaling Beyond 6 Pages

- **10 pages**: Expand Hero's Journey stages across more pages
- **20 pages**: Break into 3 acts with granular stage divisions
- **30+ pages**: Structure as multi-volume series (NSL 1.1 supports this)
- **Recommendation**: For 20+ pages, break into 6-10 page segments each following the full NSI process

## Available Commands

| Command | Phase | Purpose |
|---------|-------|---------|
| `/nsi4-start` | Setup | Create project structure, copy templates |
| `/nsi4-interview` | 1 | 20-question LoreBook interview |
| `/nsi4-bucket` | 2 | Distill LoreBook into artifacts |
| `/nsi4-frameworks` | 3 | Install cognitive frameworks |
| `/nsi4-generate` | 4 | Reverse story generation (page5 to page0) |
| `/nsi4-refine` | 5 | Refinement passes |
| `/nsi4-export` | NSL | Convert bucket to/from .nsl XML |
