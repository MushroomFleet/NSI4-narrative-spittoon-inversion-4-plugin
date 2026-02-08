---
description: Distill the LoreBook into structured bucket artifacts (world, characters, speech styles, specs)
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Task
argument-hint: "[artifacts|technical|all]"
---

## Context

You are executing NSI4 Phase 2: Bucket Artifact Creation.

LoreBook status: !`head -10 bucket/LoreBook.md 2>/dev/null || echo "ERROR: No LoreBook found. Run /nsi4-interview first."`
Existing bucket files: !`ls bucket/ 2>/dev/null`

## Your Task

Distill the information in `bucket/LoreBook.md` into specialized, structured artifacts. This command uses the bucket-builder agent for structured creation.

### If no argument or "all":
Generate both core narrative artifacts AND technical artifacts.

### If "artifacts":
Generate only core narrative artifacts (world.md, characters.md, speechstyles.md).

### If "technical":
Generate only technical artifacts (JSON specs, mermaid diagrams, glossary).

### Step 1: Read LoreBook

Read `bucket/LoreBook.md` completely. Identify:
- World-building information
- Character details
- Speech patterns and dialogue examples
- Technical systems or structures
- Terminology unique to this universe

### Step 2: Generate Core Narrative Artifacts

Use the bucket-builder agent (via Task tool) to create:

**`bucket/world.md`** — Replace the template with comprehensive world-building:
- Physical setting and geography
- Historical context
- Cultural norms and social structures
- Technology level or magic systems
- Political/economic systems
- Unique universe elements
- Wrap content in `<World>` tags (matching template convention)

**`bucket/characters.md`** — Replace the template with full character profiles:
- Name, age, heritage
- Description (physical appearance, background)
- Role in the story
- Personality traits and quirks
- Motivations and goals
- Relationships with other characters
- Wrap in `<Characters>` tags with `<charactername>` sub-tags

**`bucket/speechstyles.md`** — Replace the template with per-character speech styles:
- Vocabulary level (casual, formal, technical)
- Sentence structure preferences
- Common verbal tics, filler words, phrases
- Use of contractions and slang
- Emotional expression patterns
- Cultural/background speech influences
- Wrap in `<SpeechStyles>` tags with `<characternameSpeech>` sub-tags

### Step 3: Generate Technical Artifacts

**Mermaid Diagrams** — Create 2-5 `.mermaid` files in `bucket/`:
- Character relationship map
- Power/authority structures
- Key system flowcharts (technology, magic, politics)
- Location hierarchy
- Timeline of major events

**JSON Specifications** — Create 2-4 `.json` files in `bucket/`:
- Location details
- Equipment/technology inventory
- Character attributes (expanded)
- Cultural or organizational structures

**Glossary** — Create `bucket/[universe-name]-glossary.txt`:
- Universe-exclusive terms
- In-world jargon and slang
- Place names with descriptions
- Cultural concepts
- Technology/magic terminology

### Step 4: Validate

After generating all artifacts:
1. List all created/updated files
2. Verify each file has substantive content (not just template placeholders)
3. Suggest running `/nsi4-frameworks` as the next step

Do not modify the cognitive framework files (NarrativeSpittoon.md, GhostWritingStyle.md, HolographicTutor.md) — those are handled by `/nsi4-frameworks`.
