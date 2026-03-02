# Bucket CORE Template Protection Plan

## Description

The NSI-4 plugin uses three **CORE cognitive framework files** that must be preserved verbatim during project initialization and throughout the entire pipeline. A critical defect causes these files to be **rewritten through LLM interpretation** instead of **copied byte-for-byte**, resulting in semantic inversion of key instructions — most notably, the "because, but, therefore" narrative strategy being flattened into "avoid because, but, therefore," which is the opposite instruction.

This plan addresses the root cause, catalogs all affected code paths, and provides exact implementation changes to guarantee CORE file immutability.

---

## Functionality

### Problem Statement

Three bucket files are **CORE cognitive frameworks** — they are finished artifacts that guide story generation and must never be altered:

| File | Purpose | Risk |
|------|---------|------|
| `NarrativeSpittoon.md` | "Because, but, therefore" implicit narrative strategy | Meaning inversion during paraphrase |
| `GhostWritingStyle.md` | Prose mechanics and dialogue rules | Rule distortion during paraphrase |
| `HolographicTutor.md` | Quality assessment with 4 evaluation functions | Function specification drift |

The remaining bucket files (`Characters.md`, `SpeechStyles.md`, `World.md`, `project-instructions.md`) are **templates** — designed to be overwritten with LoreBook-derived content.

### Root Cause

The `/nsi4-start` command (line 30) instructs:

> "Read each template from `${CLAUDE_PLUGIN_ROOT}/bucket/` and write it to the project's `bucket/` directory"

This is a **Read → LLM processing → Write** operation. When Claude reads `NarrativeSpittoon.md`, which contains the nuanced instruction to *use the narrative strategy named after* "because, but, therefore" while *avoiding those explicit connector words*, the LLM can collapse this into "avoid because, but, therefore" — a semantic inversion. The file says:

> "By not overtly using 'because,' 'but,' and 'therefore,' my narrative becomes more engaging"

This describes the **implementation technique** (embed causality implicitly), not the **framework identity** (which IS the because/but/therefore strategy). When paraphrased, the distinction is lost.

### Cascade Effects

Once a CORE file is corrupted at copy time, every downstream command consumes the corrupted version:

```
/nsi4-start (CORRUPTS here)
    ↓
/nsi4-frameworks (reads corrupted copy, validates structure only — passes)
    ↓
/nsi4-generate (reads corrupted framework — writes inverted prose)
    ↓
/nsi4-refine smoothing (enforces corrupted rules — reinforces inversion)
    ↓
/nsi4-refine environment (applies corrupted style — compounds errors)
```

### Affected Code Paths — Full Assessment

#### 1. `commands/nsi4-start.md` — PRIMARY DEFECT

- **Lines 28-39**: Instructs Read+Write for ALL seven bucket files indiscriminately
- **Problem**: No distinction between CORE (verbatim) and TEMPLATE (can be rewritten) files
- **Severity**: CRITICAL — this is where corruption originates
- **Tools available**: Bash, Write, Read, Glob — Bash CAN be used for literal `cp`

#### 2. `commands/nsi4-frameworks.md` — SECONDARY DEFECT

- **Line 32**: "read the canonical version from `${CLAUDE_PLUGIN_ROOT}/bucket/` and write it to the project's `bucket/`"
- **Problem**: Same Read+Write paraphrase risk when restoring missing CORE files
- **Severity**: HIGH — meant as a safety net but has the same flaw

#### 3. `commands/nsi4-bucket.md` — UNPROTECTED BOUNDARY

- **Line 102**: "Do not modify the cognitive framework files" — text instruction only
- **Problem**: No enforcement mechanism; relies on agent compliance
- **Severity**: MEDIUM — bucket-builder agent could still overwrite CORE files

#### 4. `agents/bucket-builder.md` — MISSING GUARDRAIL

- **Lines 1-30**: Agent definition with Write tool access
- **Problem**: No explicit instruction to avoid writing to CORE files
- **Severity**: MEDIUM — agent has Write access to the entire bucket/ directory

#### 5. `hooks/hooks.json` — MISSING PROTECTION

- **Lines 1-15**: Only validates `STORY/page*.md` writes
- **Problem**: No hook prevents writes to CORE bucket files after initialization
- **Severity**: MEDIUM — no last-line defense for CORE file integrity

#### 6. `commands/nsi4-generate.md` — READ-ONLY (safe)

- Reads CORE files but never writes to them
- **Severity**: NONE — but consumes corrupted content if upstream fails

#### 7. `commands/nsi4-refine.md` — READ-ONLY (safe)

- Reads CORE files for guidance but never writes to them
- **Severity**: NONE — but applies corrupted rules if upstream fails

---

## Technical Implementation

### Architecture: Two-Tier Bucket File Classification

```
bucket/
├── CORE FILES (immutable — literal copy only)
│   ├── NarrativeSpittoon.md
│   ├── GhostWritingStyle.md
│   └── HolographicTutor.md
│
└── TEMPLATE FILES (mutable — overwritten from LoreBook)
    ├── Characters.md
    ├── SpeechStyles.md
    ├── World.md
    └── project-instructions.md
```

### Change 1: `commands/nsi4-start.md` — Use Bash `cp` for CORE files

**Current** (lines 28-39):
```markdown
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
```

**Replace with**:
```markdown
### Step 2: Copy CORE Cognitive Frameworks (Verbatim)

The following three files are **CORE cognitive frameworks** that MUST be copied byte-for-byte using the Bash tool. Do NOT use Read+Write — that passes content through LLM interpretation and risks semantic distortion. Use a literal file copy command:

```bash
cp "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle.md" bucket/GhostWritingStyle.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
```

These files are finished artifacts — do not read, interpret, summarize, or rewrite them.

### Step 3: Copy Mutable Templates

Read each of the following templates from `${CLAUDE_PLUGIN_ROOT}/bucket/` and write it to the project's `bucket/` directory. These are placeholder templates that will be replaced during `/nsi4-bucket`:

- `Characters.md` — Character profile template (replaced by /nsi4-bucket)
- `SpeechStyles.md` — Speech pattern template (replaced by /nsi4-bucket)
- `World.md` — World-building template (replaced by /nsi4-bucket)
- `project-instructions.md` — Project manifest template (replaced by /nsi4-frameworks)

### Step 4: Verify CORE File Integrity

After copying, verify the three CORE files were copied correctly by running:

```bash
diff "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
diff "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle.md" bucket/GhostWritingStyle.md
diff "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
```

If any diff produces output, the copy failed — re-run the `cp` command for that file.
```

**Step numbering update**: Renumber "Confirm Setup" from Step 3 to Step 5.

---

### Change 2: `commands/nsi4-frameworks.md` — Use Bash `cp` for CORE restoration

**Current** (line 32):
```markdown
If any framework is missing or contains only template content, read the canonical version from `${CLAUDE_PLUGIN_ROOT}/bucket/` and write it to the project's `bucket/`.
```

**Replace with**:
```markdown
If any framework is missing or contains only template content, restore it using a literal file copy via Bash — do NOT use Read+Write, as LLM interpretation can distort the framework's meaning:

```bash
cp "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle.md" bucket/GhostWritingStyle.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
```

Only copy the specific file(s) that are missing or incomplete. After restoring, verify with `diff` against the canonical source.
```

**Also add `Bash` to the allowed-tools list** in the frontmatter:
```yaml
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
```

---

### Change 3: `agents/bucket-builder.md` — Add explicit CORE file prohibition

**After line 138** (after the "Quality Standards" section, before the closing), add:

```markdown
### Protected Files — DO NOT MODIFY

The following files are CORE cognitive frameworks. You must NEVER write to, edit, overwrite, or recreate these files under any circumstances:

- `bucket/NarrativeSpittoon.md`
- `bucket/GhostWritingStyle.md`
- `bucket/HolographicTutor.md`

These files are installed by `/nsi4-start` and managed by `/nsi4-frameworks`. Your scope is limited to: `world.md`, `characters.md`, `speechstyles.md`, technical artifacts (`.json`, `.mermaid`), and the glossary (`.txt`).
```

---

### Change 4: `hooks/hooks.json` — Add CORE file write protection

**Current**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "If the file being written matches the pattern STORY/page*.md, verify that: (1) A bucket/ directory exists in the project with at least project-instructions.md, world.md, characters.md, and speechstyles.md files. (2) The content being written is narrative prose (not template content or empty). If bucket files are missing, respond with 'BLOCK: Cannot write story pages without a complete bucket. Run /nsi4-frameworks first.' Otherwise allow the write to proceed by responding with nothing."
          }
        ]
      }
    ]
  }
}
```

**Replace with**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Check TWO conditions for this Write operation: (1) CORE FILE PROTECTION: If the file being written matches bucket/NarrativeSpittoon.md, bucket/GhostWritingStyle.md, or bucket/HolographicTutor.md AND those files already exist with content, respond with 'BLOCK: Cannot overwrite CORE cognitive framework files with Write tool. These files must only be copied via Bash cp from the plugin source. If you need to restore them, use: cp ${CLAUDE_PLUGIN_ROOT}/bucket/[filename] bucket/[filename]'. (2) STORY PAGE VALIDATION: If the file being written matches the pattern STORY/page*.md, verify that: (a) A bucket/ directory exists in the project with at least project-instructions.md, world.md, characters.md, and speechstyles.md files. (b) The content being written is narrative prose (not template content or empty). If bucket files are missing, respond with 'BLOCK: Cannot write story pages without a complete bucket. Run /nsi4-frameworks first.' If neither condition applies, allow the write to proceed by responding with nothing."
          }
        ]
      },
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "If the file being edited matches bucket/NarrativeSpittoon.md, bucket/GhostWritingStyle.md, or bucket/HolographicTutor.md, respond with 'BLOCK: Cannot edit CORE cognitive framework files. These are immutable artifacts managed by /nsi4-start and /nsi4-frameworks only via literal file copy.' Otherwise allow the edit to proceed by responding with nothing."
          }
        ]
      }
    ]
  }
}
```

---

### Change 5: `commands/nsi4-bucket.md` — Strengthen CORE file warning

**Current** (line 102):
```markdown
Do not modify the cognitive framework files (NarrativeSpittoon.md, GhostWritingStyle.md, HolographicTutor.md) — those are handled by `/nsi4-frameworks`.
```

**Replace with**:
```markdown
### CORE File Immutability Rule

**DO NOT** write to, edit, overwrite, or recreate these CORE cognitive framework files:
- `bucket/NarrativeSpittoon.md`
- `bucket/GhostWritingStyle.md`
- `bucket/HolographicTutor.md`

These are immutable artifacts copied verbatim from the plugin source during `/nsi4-start`. They must never pass through LLM interpretation. If they are missing or corrupted, the user must run `/nsi4-frameworks` to restore them via literal file copy.
```

---

### Change 6: Update `commands/nsi4-start.md` output format

**Current** (lines 50-66):
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
```

**Replace with**:
```
NSI4 Project Initialized: [project-name or current directory]

Created:
  bucket/
    NarrativeSpittoon.md   (CORE — verbatim copy ✓)
    GhostWritingStyle.md   (CORE — verbatim copy ✓)
    HolographicTutor.md    (CORE — verbatim copy ✓)
    Characters.md          (template — fill during /nsi4-bucket)
    SpeechStyles.md        (template — fill during /nsi4-bucket)
    World.md               (template — fill during /nsi4-bucket)
    project-instructions.md (manifest template — fill during /nsi4-frameworks)
  STORY/
    (empty — pages will be generated during /nsi4-generate)

CORE integrity: All 3 cognitive frameworks verified against source.
```

---

## Data Model

### File Classification Enum

| Classification | Copy Method | Modified By | Protected By |
|----------------|-------------|-------------|--------------|
| `CORE` | Bash `cp` (literal) | Nothing — immutable | Hook + instructions |
| `TEMPLATE` | Read+Write (LLM) | `/nsi4-bucket`, `/nsi4-frameworks` | None needed |
| `GENERATED` | Agent creates | bucket-builder agent | None needed |
| `STORY` | LLM generates | `/nsi4-generate`, `/nsi4-refine` | Story page hook |

### CORE Files — Canonical Source

```
Source: ${CLAUDE_PLUGIN_ROOT}/bucket/
├── NarrativeSpittoon.md   (27 lines, <NarrativeSpittoon> tags)
├── GhostWritingStyle.md   (33 lines, <GhostWritingStyle> tags)
└── HolographicTutor.md    (80 lines, <HolographicTutor> tags)
```

These files at the plugin source location are the **single source of truth**. Project copies are always derived from these via `cp`.

---

## Testing Scenarios

### Test 1: Fresh Project Initialization
1. Run `/nsi4-start test-project`
2. Verify `bucket/NarrativeSpittoon.md` is byte-identical to source: `diff "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" test-project/bucket/NarrativeSpittoon.md`
3. Repeat for `GhostWritingStyle.md` and `HolographicTutor.md`
4. All three diffs must produce zero output

### Test 2: CORE File Write Block
1. Initialize a project with `/nsi4-start`
2. Attempt to use Write tool on `bucket/NarrativeSpittoon.md`
3. Hook must respond with BLOCK message
4. File must remain unchanged

### Test 3: CORE File Edit Block
1. Initialize a project with `/nsi4-start`
2. Attempt to use Edit tool on `bucket/GhostWritingStyle.md`
3. Hook must respond with BLOCK message
4. File must remain unchanged

### Test 4: Framework Restoration
1. Delete `bucket/NarrativeSpittoon.md` from a project
2. Run `/nsi4-frameworks`
3. Verify restored file is byte-identical to source via `diff`

### Test 5: Bucket Builder Compliance
1. Run `/nsi4-bucket` with a populated LoreBook
2. Verify the three CORE files are untouched after bucket-builder completes
3. Verify `world.md`, `characters.md`, `speechstyles.md` ARE properly generated

### Test 6: Semantic Integrity Check
1. After initialization, search for "Implicit Causality" in `bucket/NarrativeSpittoon.md`
2. Verify the phrase "Substituting 'Because'" appears (not "Avoiding 'Because'")
3. Verify "By not overtly using" appears in the Aims section (this is the technique description, not the framework identity)

---

## Implementation Sequence

### Phase 1: Core Protection (Changes 1, 2)
Modify `nsi4-start.md` and `nsi4-frameworks.md` to use `cp` for CORE files. This eliminates the root cause.

**Files modified:**
- `commands/nsi4-start.md`
- `commands/nsi4-frameworks.md`

### Phase 2: Enforcement Layer (Changes 3, 4, 5)
Add hook-based write protection and explicit agent guardrails. This prevents future regressions.

**Files modified:**
- `hooks/hooks.json`
- `agents/bucket-builder.md`
- `commands/nsi4-bucket.md`

### Phase 3: Verification (Change 6)
Update output format to confirm CORE file integrity during initialization.

**Files modified:**
- `commands/nsi4-start.md` (output section)

### Phase 4: Validation
Run all six testing scenarios to confirm the fix.

---

## Summary of All File Changes

| File | Change | Phase |
|------|--------|-------|
| `commands/nsi4-start.md` | Split Step 2 into CORE (cp) + TEMPLATE (Read+Write), add diff verification, update output format | 1, 3 |
| `commands/nsi4-frameworks.md` | Add Bash to allowed-tools, use cp for CORE restoration | 1 |
| `agents/bucket-builder.md` | Add "Protected Files" section prohibiting CORE file writes | 2 |
| `hooks/hooks.json` | Add Write protection for CORE files, add Edit matcher for CORE files | 2 |
| `commands/nsi4-bucket.md` | Strengthen CORE file warning to explicit immutability rule | 2 |

**Total files modified: 5**
**No new files created** (beyond this plan document)
**No files deleted**
