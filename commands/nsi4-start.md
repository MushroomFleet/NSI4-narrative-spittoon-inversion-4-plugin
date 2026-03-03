---
description: Initialize a new NSI4 story project with folder structure and bucket templates
allowed-tools:
  - Bash
  - Write
  - Read
  - Glob
argument-hint: "[project-name] [--ghost path/to/custom-ghost.md]"
---

## Context

You are initializing a new Narrative Spittoon Inversion 4.0 project.

Current working directory: !`pwd`
Existing contents: !`ls -la 2>/dev/null || dir 2>/dev/null`

## Your Task

Create an NSI4 project structure. If a project-name argument is provided, create it as a subdirectory. If no argument, create structure in the current directory.

### Argument Parsing

Parse the arguments for two optional components:
- **project-name**: Any argument that is NOT `--ghost` and does NOT immediately follow `--ghost`. Used as the subdirectory name.
- **`--ghost <path>`**: When present, the next argument is the path to a user-supplied custom GhostWritingStyle.md file. This overrides the default CORE version.

Examples:
- `/nsi4-start` — current directory, default ghost
- `/nsi4-start my-story` — subdirectory "my-story", default ghost
- `/nsi4-start --ghost ~/my-ghost.md` — current directory, custom ghost
- `/nsi4-start my-story --ghost ~/my-ghost.md` — subdirectory "my-story", custom ghost

If `--ghost` is provided, validate the path before proceeding:
```bash
test -f "<ghost-path>" && grep -q "<GhostWritingStyle>" "<ghost-path>" && echo "VALID" || echo "INVALID"
```
If INVALID, stop and report: "ERROR: The --ghost file must exist and contain `<GhostWritingStyle>` tags."

### Step 1: Create Directory Structure

Create these directories:
- `bucket/` — Will contain all narrative artifacts
- `STORY/` — Will contain generated story pages

### Step 2: Copy CORE Cognitive Frameworks (Verbatim)

The following files are **CORE cognitive frameworks** that MUST be copied byte-for-byte using the Bash tool. Do NOT use Read+Write — that passes content through LLM interpretation and risks semantic distortion.

**Always copy from plugin source:**
```bash
cp "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle-sentence.md" bucket/GhostWritingStyle-sentence.md
```

**GhostWritingStyle.md — conditional source:**

If `--ghost <path>` was provided and validated:
```bash
cp "<ghost-path>" bucket/GhostWritingStyle.md
```

If `--ghost` was NOT provided (default):
```bash
cp "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle.md" bucket/GhostWritingStyle.md
```

All four files are finished artifacts — do not read, interpret, summarize, or rewrite them. The custom ghost file receives the same immutability protections as the default. GhostWritingStyle-sentence.md is always installed from the plugin source regardless of --ghost usage.

### Step 3: Copy Mutable Templates

Read each of the following templates from `${CLAUDE_PLUGIN_ROOT}/bucket/` and write it to the project's `bucket/` directory. These are placeholder templates that will be replaced during `/nsi4-bucket`:

- `Characters.md` — Character profile template (replaced by /nsi4-bucket)
- `SpeechStyles.md` — Speech pattern template (replaced by /nsi4-bucket)
- `World.md` — World-building template (replaced by /nsi4-bucket)
- `project-instructions.md` — Project manifest template (replaced by /nsi4-frameworks)

### Step 4: Verify CORE File Integrity

After copying, verify the four CORE files were copied correctly by running diff against their respective sources:

**Always diff against plugin source:**
```bash
diff "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
diff "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
diff "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle-sentence.md" bucket/GhostWritingStyle-sentence.md
```

**GhostWritingStyle.md — diff against the source that was used:**

If `--ghost <path>` was provided:
```bash
diff "<ghost-path>" bucket/GhostWritingStyle.md
```

If default was used:
```bash
diff "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle.md" bucket/GhostWritingStyle.md
```

If any diff produces output, the copy failed — re-run the `cp` command for that file.

### Step 5: Confirm Setup

After creating the structure, display:
1. The created directory tree
2. A brief explanation of next steps
3. Suggest running `/nsi4-interview` to begin the process

### Output Format

If `--ghost` was NOT used (default):
```
NSI4 Project Initialized: [project-name or current directory]

Created:
  bucket/
    NarrativeSpittoon.md   (CORE — verbatim copy ✓)
    GhostWritingStyle.md   (CORE — verbatim copy ✓)
    GhostWritingStyle-sentence.md (CORE — verbatim copy ✓)
    HolographicTutor.md    (CORE — verbatim copy ✓)
    Characters.md          (template — fill during /nsi4-bucket)
    SpeechStyles.md        (template — fill during /nsi4-bucket)
    World.md               (template — fill during /nsi4-bucket)
    project-instructions.md (manifest template — fill during /nsi4-frameworks)
  STORY/
    (empty — pages will be generated during /nsi4-generate)

CORE integrity: All 4 cognitive frameworks verified against source.
Next step: Run /nsi4-interview to begin the 20-question LoreBook interview.
```

If `--ghost <path>` was used:
```
NSI4 Project Initialized: [project-name or current directory]

Created:
  bucket/
    NarrativeSpittoon.md   (CORE — verbatim copy ✓)
    GhostWritingStyle.md   (CORE — custom ghost ✓) ← [source path]
    GhostWritingStyle-sentence.md (CORE — verbatim copy ✓)
    HolographicTutor.md    (CORE — verbatim copy ✓)
    Characters.md          (template — fill during /nsi4-bucket)
    SpeechStyles.md        (template — fill during /nsi4-bucket)
    World.md               (template — fill during /nsi4-bucket)
    project-instructions.md (manifest template — fill during /nsi4-frameworks)
  STORY/
    (empty — pages will be generated during /nsi4-generate)

CORE integrity: 3 default + 1 custom cognitive frameworks verified.
Next step: Run /nsi4-interview to begin the 20-question LoreBook interview.
```

Do not do anything else beyond creating the structure and confirming.
