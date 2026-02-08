---
description: Initialize a new NSI4 story project with folder structure and bucket templates
allowed-tools:
  - Bash
  - Write
  - Read
  - Glob
argument-hint: "[project-name]"
---

## Context

You are initializing a new Narrative Spittoon Inversion 4.0 project.

Current working directory: !`pwd`
Existing contents: !`ls -la 2>/dev/null || dir 2>/dev/null`

## Your Task

Create an NSI4 project structure. If a project-name argument is provided, create it as a subdirectory. If no argument, create structure in the current directory.

### Step 1: Create Directory Structure

Create these directories:
- `bucket/` — Will contain all narrative artifacts
- `STORY/` — Will contain generated story pages

### Step 2: Copy Bucket Templates

Copy the template files from the plugin's bucket templates into the project's `bucket/` folder. Read each template from `${CLAUDE_PLUGIN_ROOT}/bucket/` and write it to the project's `bucket/` directory:

Templates to copy:
- `Characters.md` — Character profile template
- `SpeechStyles.md` — Speech pattern template
- `World.md` — World-building template
- `NarrativeSpittoon.md` — Narrative framework
- `GhostWritingStyle.md` — Writing style guide
- `HolographicTutor.md` — Quality assessment system
- `project-instructions.md` — Project manifest template

### Step 3: Confirm Setup

After creating the structure, display:
1. The created directory tree
2. A brief explanation of next steps
3. Suggest running `/nsi4-interview` to begin the process

### Output Format

```
NSI4 Project Initialized: [project-name or current directory]

Created:
  bucket/
    Characters.md          (template — fill during /nsi4-bucket)
    SpeechStyles.md        (template — fill during /nsi4-bucket)
    World.md               (template — fill during /nsi4-bucket)
    NarrativeSpittoon.md   (cognitive framework — ready)
    GhostWritingStyle.md   (cognitive framework — ready)
    HolographicTutor.md    (cognitive framework — ready)
    project-instructions.md (manifest template — fill during /nsi4-frameworks)
  STORY/
    (empty — pages will be generated during /nsi4-generate)

Next step: Run /nsi4-interview to begin the 20-question LoreBook interview.
```

Do not do anything else beyond creating the structure and confirming.
