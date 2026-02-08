# Narrative Spittoon Inversion 4.0 Plugin

## Overview

This is a Claude Code plugin implementing the Narrative Spittoon Inversion (NSI) 4.0 workflow — an AI-assisted story creation methodology using reverse chronological generation.

## Commands

- `/nsi4-start [name]` — Initialize project structure
- `/nsi4-interview` — 20-question LoreBook interview
- `/nsi4-bucket` — Distill LoreBook into artifacts
- `/nsi4-frameworks` — Install cognitive frameworks
- `/nsi4-generate` — Reverse story generation (page5 to page0)
- `/nsi4-refine [pass]` — Refinement passes
- `/nsi4-export [import|export]` — NSL 1.1 conversion

## Architecture

- `bucket/` templates are copied to new projects by /nsi4-start
- Three cognitive frameworks guide generation quality
- Story pages are generated in reverse order with approval gates
- NSL 1.1 XML format for import/export portability

## Key Files

- `skills/nsi4-workflow/SKILL.md` — Core workflow knowledge
- `scripts/nsl-converter.py` — NSL XML converter (requires Python 3.6+)
- `bucket/` — Template files for new projects
- `docs/` — Original specification documents
