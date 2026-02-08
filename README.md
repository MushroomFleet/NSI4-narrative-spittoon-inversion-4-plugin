# Narrative Spittoon Inversion 4.0 — Claude Code Plugin

**AI-assisted story creation using reverse chronological generation**

[![Version](https://img.shields.io/badge/version-4.0.0-blue.svg)](https://github.com/MushroomFleet/NSI4-narrative-spittoon-inversion-4-plugin)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-blueviolet.svg)](https://claude.ai/code)

---

## Overview

Narrative Spittoon Inversion (NSI) is a structured methodology for AI-assisted fiction writing that generates stories **in reverse chronological order** — from the ending to the beginning. This approach produces tightly plotted narratives where every scene is purpose-built to serve the story's conclusion.

This Claude Code plugin implements NSI 4.0 as a complete guided workflow with slash commands, specialized agents, cognitive frameworks, and full NSL 1.1 import/export support.

### Why Write in Reverse?

Traditional AI story generation drifts. Characters wander, subplots emerge without payoff, and endings feel disconnected from beginnings. NSI eliminates these problems by inverting the process:

1. **Start with the ending** — Know exactly where the story lands
2. **Work backward** — Each page answers "what led to the next page's events?"
3. **Map the Hero's Journey in reverse** — Classical structure emerges naturally
4. **Every scene has purpose** — Nothing exists without paying off later

The result: stories that read forward with the inevitability of a chain reaction, because every link was forged from the conclusion backward.

---

## Installation

### Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed and configured
- Python 3.6+ (required only for NSL import/export via `/nsi4-export`)

### Install the Plugin

```bash
claude plugins add https://github.com/MushroomFleet/NSI4-narrative-spittoon-inversion-4-plugin
```

Or clone and install locally:

```bash
git clone https://github.com/MushroomFleet/NSI4-narrative-spittoon-inversion-4-plugin.git
claude plugins add ./NSI4-narrative-spittoon-inversion-4-plugin
```

---

## Quick Start

```bash
# 1. Create a new story project
/nsi4-start my-story

# 2. Run the 20-question LoreBook interview
/nsi4-interview

# 3. Distill LoreBook into world, characters, speech styles
/nsi4-bucket

# 4. Install cognitive frameworks and generate manifest
/nsi4-frameworks

# 5. Generate the story in reverse (page5 → page0)
/nsi4-generate

# 6. Run quality assessment and refinement passes
/nsi4-refine score
/nsi4-refine speech

# 7. Export to portable NSL format
/nsi4-export export
```

---

## Commands

| Command | Phase | Description |
|---------|-------|-------------|
| `/nsi4-start [name]` | Setup | Create project structure with `bucket/` and `STORY/` folders, copy template files |
| `/nsi4-interview` | Phase 1 | Run a dynamic 20-question interview to build `LoreBook.md` |
| `/nsi4-bucket [all\|artifacts\|technical]` | Phase 2 | Distill the LoreBook into world, character, speech style, and technical artifacts |
| `/nsi4-frameworks` | Phase 3 | Verify/install cognitive frameworks and generate `project-instructions.md` manifest |
| `/nsi4-generate [page-number]` | Phase 4 | Reverse-generate story pages with approval gates between each |
| `/nsi4-refine [pass]` | Phase 5 | Run refinement passes: `score`, `speech`, `repetition`, `smoothing`, `environment`, `all` |
| `/nsi4-export [export\|import] [path]` | NSL | Convert between bucket folder and NSL 1.1 XML format |

---

## The 5-Phase Workflow

### Phase 1: Knowledge Gathering

`/nsi4-interview` conducts a guided 20-question interview covering:
- Universe and setting (world, time period, physical laws, society)
- Characters (cast, personalities, motivations, relationships)
- Story and plot (central conflict, stakes, key events)
- The ending (how the story concludes — critical for reverse generation)
- Tone and themes (atmosphere, genre, thematic depth)

Each answer is saved incrementally to `bucket/LoreBook.md`. Use `/nsi4-interview resume` to continue a previously started interview.

### Phase 2: Bucket Artifact Creation

`/nsi4-bucket` distills the LoreBook into structured artifacts:

| Artifact | Format | Purpose |
|----------|--------|---------|
| `world.md` | Markdown with `<World>` tags | Setting, geography, history, culture, systems |
| `characters.md` | Markdown with `<Characters>` tags | Character profiles, personality, quirks, motivations |
| `speechstyles.md` | Markdown with `<SpeechStyles>` tags | Per-character speech patterns, verbal tics, vocabulary |
| `*.json` | JSON | Technical specifications (locations, equipment, systems) |
| `*.mermaid` | Mermaid | Diagrams (character relationships, power structures, timelines) |
| `*-glossary.txt` | Plain text | Universe-specific terminology and definitions |

### Phase 3: Core Framework Setup

`/nsi4-frameworks` installs three cognitive frameworks that guide AI generation quality:

**NarrativeSpittoon.md** — Controls narrative technique by replacing explicit logical connectors ("because", "but", "therefore") with implicit storytelling:
- Implicit Causality: Embed motivations through dialogue, action, description
- Subtle Conflict: Introduce complications through narrative shifts
- Organic Consequences: Let outcomes unfold through progression

**GhostWritingStyle.md** — Controls writing mechanics:
- Sentence variety, natural dialogue, speaker rotation
- Pauses, hesitations, filler words for realistic speech
- Active voice, vivid imagery, balanced pacing

**HolographicTutor.md** — Quality assessment system with four functions:
- **Score**: Numerical rating out of 100 with justification
- **Review**: Academic analysis with specific examples
- **Critic**: Publisher perspective with market viability
- **Weakness**: 3 areas needing improvement (quotes, no suggestions)

### Phase 4: Story Generation — The Inversion

`/nsi4-generate` creates the story in reverse, with user approval between each page:

| Generation Order | Page | Hero's Journey Stage | Story Function |
|:---:|:---:|---|---|
| 1st | Page 5 | Return with Elixir / Resolution | Ending — transformation complete |
| 2nd | Page 4 | Resurrection / Climax | Final challenge, ultimate test |
| 3rd | Page 3 | Road Back / Rising Action | Consequences unfold, stakes escalate |
| 4th | Page 2 | Ordeal / Commitment | Major challenge, point of no return |
| 5th | Page 1 | Tests, Allies, Enemies / Setup | World establishment, character intro |
| 6th | Page 0 | Ordinary World / Opening | Beginning — initial state |

Each page targets 800-1500 words, references all bucket files for consistency, and applies all three cognitive frameworks.

### Phase 5: Refinement

`/nsi4-refine` runs optional polish passes (recommended order):

1. **Quality Assessment** (`score`) — Score each page using HolographicTutor
2. **Speech Style** (`speech`) — Verify character voice consistency against speechstyles.md
3. **Repetition Sniper** (`repetition`) — Eliminate redundant phrasing across all pages
4. **Narrative Smoothing** (`smoothing`) — Polish transitions and fix reverse-generation seams
5. **Environmental Enhancement** (`environment`) — Deepen sensory details and atmosphere

---

## Agents

### Holographic Tutor

Triggered by: "score my story", "review my writing", "critique this page", "find weaknesses", "assess quality"

Provides on-demand quality assessment using Score, Review, Critic, or Weakness functions at college graduate level.

### Bucket Builder

Triggered by: "create bucket artifacts", "distill the LoreBook", "generate world building files", "create character profiles"

Specializes in transforming raw LoreBook content into structured narrative artifacts with proper XML-style tagging.

---

## NSL 1.1 Format

The Narrative Spittoon Language (NSL) is an XML-based format that packages an entire narrative bucket into a single portable `.nsl` file.

### Export

```bash
/nsi4-export export
# Creates [project-name].nsl from bucket/ and STORY/ folders
```

### Import

```bash
/nsi4-export import path/to/story.nsl
# Extracts .nsl file into bucket/ and STORY/ folders
```

### Manual Conversion (Python)

```bash
python scripts/nsl-converter.py export --bucket ./bucket --story ./STORY --output story.nsl
python scripts/nsl-converter.py import --input story.nsl --bucket ./bucket --story ./STORY
```

For the complete NSL 1.1 specification, see [docs/NSL-1.1-specification.md](docs/NSL-1.1-specification.md).

---

## Project Structure

```
narrative-spittoon-inversion/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── commands/
│   ├── nsi4-start.md            # Project initialization
│   ├── nsi4-interview.md        # LoreBook interview
│   ├── nsi4-bucket.md           # Artifact creation
│   ├── nsi4-frameworks.md       # Framework setup
│   ├── nsi4-generate.md         # Reverse story generation
│   ├── nsi4-refine.md           # Refinement passes
│   └── nsi4-export.md           # NSL import/export
├── agents/
│   ├── holographic-tutor.md     # Quality assessment agent
│   └── bucket-builder.md        # Artifact creation agent
├── skills/
│   └── nsi4-workflow/
│       ├── SKILL.md             # Core methodology knowledge
│       └── references/
│           ├── heros-journey-mapping.md
│           ├── refinement-passes.md
│           ├── cognitive-frameworks.md
│           ├── nsi4-process-guide.md
│           └── nsl-1.1-specification.md
├── hooks/
│   └── hooks.json               # Story page validation hook
├── scripts/
│   └── nsl-converter.py         # NSL XML converter (Python 3.6+)
├── bucket/                      # Template files for new projects
│   ├── Characters.md
│   ├── SpeechStyles.md
│   ├── World.md
│   ├── NarrativeSpittoon.md
│   ├── GhostWritingStyle.md
│   ├── HolographicTutor.md
│   └── project-instructions.md
├── docs/                        # Specification documents
│   ├── NSL-1.1-specification.md
│   ├── NarrativeSpittoonInversion3.0-process.md
│   └── NSI4-Plugin-implementation-plan.md
├── examples/                    # Example projects and archives
│   └── archive/
├── CLAUDE.md
├── LICENSE
└── README.md
```

---

## Scaling Beyond 6 Pages

The default 6-page structure maps cleanly to the Hero's Journey, but NSI supports scaling:

| Scale | Approach |
|-------|----------|
| **10 pages** | Expand Hero's Journey stages across more pages |
| **20 pages** | Break into 3 acts with granular stage divisions |
| **30+ pages** | Multi-volume series — each volume follows the full 6-page inversion independently |

For 20+ page projects, break into 6-10 page segments each following the complete NSI process. NSL 1.1 provides native multi-volume support with series arc tracking.

---

## Story Project Structure

When you run `/nsi4-start`, the following structure is created in your working directory:

```
your-story/
├── bucket/
│   ├── LoreBook.md              ← Built by /nsi4-interview
│   ├── world.md                 ← Generated by /nsi4-bucket
│   ├── characters.md            ← Generated by /nsi4-bucket
│   ├── speechstyles.md          ← Generated by /nsi4-bucket
│   ├── NarrativeSpittoon.md     ← Installed by /nsi4-frameworks
│   ├── GhostWritingStyle.md     ← Installed by /nsi4-frameworks
│   ├── HolographicTutor.md      ← Installed by /nsi4-frameworks
│   ├── project-instructions.md  ← Generated by /nsi4-frameworks
│   ├── *.json                   ← Generated by /nsi4-bucket
│   ├── *.mermaid                ← Generated by /nsi4-bucket
│   └── *-glossary.txt           ← Generated by /nsi4-bucket
└── STORY/
    ├── page5.md                 ← Written 1st (ending)
    ├── page4.md                 ← Written 2nd
    ├── page3.md                 ← Written 3rd
    ├── page2.md                 ← Written 4th
    ├── page1.md                 ← Written 5th
    └── page0.md                 ← Written 6th (beginning)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **4.0.0** | 2026-02 | Claude Code plugin with native file integration, slash commands, agents, hooks, NSL converter |
| 3.0 | 2025-10 | Web service workflow with copy-paste prompts |
| 2.0 | 2025 | Refined methodology with cognitive frameworks |
| 1.0 | 2024 | Original Narrative Spittoon Inversion concept |

### Key Upgrades in NSI 4.0

| Aspect | NSI 3.0 (Web Service) | NSI 4.0 (Claude Code Plugin) |
|--------|----------------------|------------------------------|
| Workflow | Copy-paste prompts to chat | Slash commands operate directly on files |
| File Management | Manual file creation | Automated project scaffolding |
| Context Loading | User re-attaches files each turn | Plugin reads bucket files automatically |
| Validation | Manual review only | Holographic Tutor agent on demand |
| Templates | User copies from docs | `/nsi4-start` copies templates automatically |
| NSL Support | None | Full import/export via Python script |
| Frameworks | User installs manually | `/nsi4-frameworks` installs and configures |

---

## License

This project is released under the [MIT License](LICENSE).

---

## Citation

### Academic Citation

If you use this codebase in your research or project, please cite:

```bibtex
@software{nsi4_narrative_spittoon_inversion,
  title = {Narrative Spittoon Inversion 4.0: AI-Assisted Story Creation Using Reverse Chronological Generation},
  author = {Drift Johnson},
  year = {2025},
  url = {https://github.com/MushroomFleet/NSI4-narrative-spittoon-inversion-4-plugin},
  version = {4.0.0}
}
```

### Donate:

[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)
