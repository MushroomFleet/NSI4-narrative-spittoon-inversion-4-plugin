---
description: Install cognitive frameworks and generate the project-instructions.md manifest
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

## Context

You are executing NSI4 Phase 3: Core Framework Setup.

Current bucket contents: !`ls bucket/ 2>/dev/null`
Frameworks present: !`ls bucket/NarrativeSpittoon.md bucket/GhostWritingStyle.md bucket/HolographicTutor.md 2>/dev/null || echo "Some frameworks missing"`

## Your Task

Verify cognitive frameworks are installed and generate the project manifest.

### Step 1: Verify Cognitive Frameworks

Check that these three files exist and contain proper content (not just template placeholders):

1. **`bucket/NarrativeSpittoon.md`** — Must contain the `<NarrativeSpittoon>` framework with Implicit Causality, Subtle Conflict Introduction, and Organic Consequences sections.

2. **`bucket/GhostWritingStyle.md`** — Must contain the `<GhostWritingStyle>` framework with writing mechanics rules.

3. **`bucket/HolographicTutor.md`** — Must contain the `<HolographicTutor>` framework with Score, Review, Critic, and Weakness functions.

If any framework is missing or contains only template content, read the canonical version from `${CLAUDE_PLUGIN_ROOT}/bucket/` and write it to the project's `bucket/`.

### Step 2: Generate Project Manifest

Read ALL files currently in `bucket/` and generate `bucket/project-instructions.md`:

```markdown
# Project Instructions: [Story Title from LoreBook]

## Cognitive Framework Definition
- NarrativeSpittoon.md - Narrative style guidelines (implicit causality, show don't tell)
- GhostWritingStyle.md - Writing style rules (dialogue, pacing, voice)
- HolographicTutor.md - Quality assessment system (4 evaluation functions: Score, Review, Critic, Weakness)

## Universe Core Documentation
- world.md - [one-line description based on content]
- [universe]-glossary.txt - [one-line description]

## Character Profiles
- characters.md - [one-line description listing character names]
- speechstyles.md - [one-line description listing character names]

## Technical Specifications
- [filename].json - [one-line description]
[list all JSON files]

## Visualization Resources
- [filename].mermaid - [one-line description]
[list all mermaid files]

## Content Structure Tags
- The setting is defined inside "world.md" in <World> tags
- Character personality definitions are in "characters.md" in <Characters> tags
- Speech patterns are defined in "speechstyles.md" in <SpeechStyles> tags

## Processing Framework
- Cross-referenced document relationships
- Technical specification integration
- Visualization resource utilization
```

### Step 3: Validate and Report

1. List all bucket files with their sizes
2. Confirm all required files are present
3. Flag any missing optional files
4. Suggest running `/nsi4-generate` as the next step

### Required Files Checklist
- [ ] LoreBook.md
- [ ] world.md (with content, not template)
- [ ] characters.md (with content, not template)
- [ ] speechstyles.md (with content, not template)
- [ ] NarrativeSpittoon.md
- [ ] GhostWritingStyle.md
- [ ] HolographicTutor.md
- [ ] project-instructions.md (just generated)
