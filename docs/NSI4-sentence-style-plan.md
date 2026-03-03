# NSI4 Sentence-Style Hybrid System — Implementation Plan

## Description

Add `GhostWritingStyle-sentence.md` as a fourth CORE cognitive framework to the NSI4 plugin, creating a two-layer style system that separates **scene-level causality** (NarrativeSpittoon.md) from **sentence-level prose style** (GhostWritingStyle-sentence.md). The existing `--ghost` flag continues to override only the template `GhostWritingStyle.md` — the sentence-level file is always installed and is not user-overridable.

### The Problem Being Solved

The original NarrativeSpittoon.md instruction — "use but/because/therefore reasoning" — was accidentally inverted during a prior fix to read "avoid but/because/therefore in prose." This produced an emergent benefit: clipped, paratactic, accumulative prose that reviewers praised as thematically coherent. However, the same inversion removed but/because/therefore as a **structural driver** at the scene and sequence level, causing negative scoring for plot coherence.

### The Hybrid Solution

| Layer | File | Directive | Scope |
|-------|------|-----------|-------|
| **Scene/Sequence** | `NarrativeSpittoon.md` | USE but/because/therefore reasoning to drive causality between story beats | Plot structure, scene connections, consequence chains |
| **Sentence/Prose** | `GhostWritingStyle-sentence.md` | AVOID literal "but/because/therefore" words in prose — use parataxis, short declaratives, additive sentence structure | Line-by-line sentence construction |
| **Writing Mechanics** | `GhostWritingStyle.md` | Dialogue flow, pacing, voice differentiation, active voice | General writing quality (overridable via `--ghost`) |

This preserves the praised prose register while restoring structural causality scoring.

---

## Functionality

### New CORE File: `GhostWritingStyle-sentence.md`

- Source file already exists at plugin root: `narrative-spittoon-standard/GhostWritingStyle-sentence.md`
- Must be copied to `bucket/GhostWritingStyle-sentence.md` in every new project
- Copied via literal `cp` (same as other CORE files — no LLM interpretation)
- Immutable after placement — protected by hooks against Write/Edit
- NOT overridable by `--ghost` (that flag only affects `GhostWritingStyle.md`)
- Used in combination with whatever `GhostWritingStyle.md` is active (default or custom)

### Interaction with Existing Components

```
┌─────────────────────────────────────────────────────────┐
│                    STORY GENERATION                      │
│                                                          │
│  Scene-Level Causality ← NarrativeSpittoon.md           │
│    "Each beat EARNS the next through consequence"        │
│    (but/because/therefore as STRUCTURAL reasoning)       │
│                                                          │
│  Sentence-Level Style ← GhostWritingStyle-sentence.md   │
│    "Never write the WORDS but/because/therefore"         │
│    (parataxis, short declaratives, additive prose)       │
│                                                          │
│  Writing Mechanics ← GhostWritingStyle.md               │
│    "Dialogue, pacing, voice, active construction"        │
│    (overridable via --ghost)                             │
│                                                          │
│  Quality Assessment ← HolographicTutor.md               │
│    "Score/Review/Critic/Weakness"                        │
└─────────────────────────────────────────────────────────┘
```

### What Does NOT Change

- `NarrativeSpittoon.md` content — unchanged, continues to drive scene-level causality
- `GhostWritingStyle.md` content — unchanged, continues as writing mechanics guide
- `HolographicTutor.md` — unchanged
- `--ghost` flag behavior — still only overrides `GhostWritingStyle.md`
- NSL 1.1 converter — addressed separately (Step 8)
- Mutable template files (Characters, SpeechStyles, World, project-instructions) — unchanged

---

## Technical Implementation

### Step 1: Copy Source File to `bucket/` Directory

The `GhostWritingStyle-sentence.md` already exists at the plugin root. It must also exist in the `bucket/` directory as the canonical source for project copying.

**Action:** Copy the file from plugin root to `bucket/`:

```bash
cp "GhostWritingStyle-sentence.md" "bucket/GhostWritingStyle-sentence.md"
```

**Validation:** The file in `bucket/` must be identical to the root file. The root copy is the authored original; `bucket/` is the distribution source used by `cp` during `/nsi4-start`.

> **Note:** The root-level `GhostWritingStyle-sentence.md` does NOT currently have `<GhostWritingStyle>` XML wrapper tags. It uses standard markdown headings. This is intentional — the sentence-style file is a separate framework from the template `GhostWritingStyle.md` and does not need the same tag structure. However, for consistency with the CORE file validation pattern, we should add a distinguishing tag. Add `<GhostWritingSentenceStyle>` wrapper tags around the content in the `bucket/` copy.

**File: `bucket/GhostWritingStyle-sentence.md`** — Wrap content:

```markdown
<GhostWritingSentenceStyle>
[existing content of GhostWritingStyle-sentence.md]
</GhostWritingSentenceStyle>
```

---

### Step 2: Update `commands/nsi4-start.md`

**File:** `commands/nsi4-start.md`

#### 2a. Add to Step 2 CORE copy block (after line 54)

**Current** (lines 50-66):
```markdown
**Always copy from plugin source:**
\```bash
cp "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
\```

**GhostWritingStyle.md — conditional source:**
...
```

**Change to:**
```markdown
**Always copy from plugin source:**
\```bash
cp "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
cp "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle-sentence.md" bucket/GhostWritingStyle-sentence.md
\```

**GhostWritingStyle.md — conditional source:**
...
```

**Rationale:** `GhostWritingStyle-sentence.md` is always copied from the plugin source. It is never overridden by `--ghost`. Add it to the unconditional copy block alongside NarrativeSpittoon.md and HolographicTutor.md.

#### 2b. Update the "finished artifacts" note (line 68)

**Current:**
```
All three files are finished artifacts — do not read, interpret, summarize, or rewrite them.
```

**Change to:**
```
All four files are finished artifacts — do not read, interpret, summarize, or rewrite them. The custom ghost file receives the same immutability protections as the default. GhostWritingStyle-sentence.md is always installed from the plugin source regardless of --ghost usage.
```

#### 2c. Add diff verification for the new file in Step 4 (after line 87)

**Current** (lines 83-87):
```markdown
\```bash
diff "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
diff "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
\```
```

**Change to:**
```markdown
\```bash
diff "${CLAUDE_PLUGIN_ROOT}/bucket/NarrativeSpittoon.md" bucket/NarrativeSpittoon.md
diff "${CLAUDE_PLUGIN_ROOT}/bucket/HolographicTutor.md" bucket/HolographicTutor.md
diff "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle-sentence.md" bucket/GhostWritingStyle-sentence.md
\```
```

#### 2d. Update output format (lines 112-150)

In **both** output format blocks (default and custom ghost), add the new file to the directory listing:

**Default output (after line 119):**
```
    GhostWritingStyle-sentence.md (CORE — verbatim copy ✓)
```

**Custom ghost output (after line 139):**
```
    GhostWritingStyle-sentence.md (CORE — verbatim copy ✓)
```

**Update CORE integrity lines:**

Default:
```
CORE integrity: All 4 cognitive frameworks verified against source.
```

Custom:
```
CORE integrity: 3 default + 1 custom cognitive frameworks verified.
```

---

### Step 3: Update `commands/nsi4-frameworks.md`

**File:** `commands/nsi4-frameworks.md`

#### 3a. Add verification check for the new file (Step 1, after line 31)

Add a fourth verification entry:

```markdown
4. **`bucket/GhostWritingStyle-sentence.md`** — Must contain the `<GhostWritingSentenceStyle>` framework with sentence-level prose style rules (parataxis, short declaratives, additive structure).
```

#### 3b. Add restoration logic (after line 42)

Add to the restoration section (after the HolographicTutor cp line):

```markdown
If `GhostWritingStyle-sentence.md` is missing or contains only template content, restore using a literal file copy:

\```bash
cp "${CLAUDE_PLUGIN_ROOT}/bucket/GhostWritingStyle-sentence.md" bucket/GhostWritingStyle-sentence.md
\```

Unlike GhostWritingStyle.md, this file has no custom override mechanism — always restore from plugin source.
```

#### 3c. Update Step 2 manifest template (line 63)

Add to the Cognitive Framework Definition section:

```markdown
- GhostWritingStyle-sentence.md - Sentence-level prose style (parataxis, declarative chains, additive structure — no literal but/because/therefore)
```

#### 3d. Update required files checklist (line 105)

Add:
```markdown
- [ ] GhostWritingStyle-sentence.md
```

---

### Step 4: Update `commands/nsi4-generate.md`

**File:** `commands/nsi4-generate.md`

#### 4a. Add to context loading list (after line 42)

**Current** (lines 41-42):
```markdown
5. `bucket/NarrativeSpittoon.md` — Narrative framework rules
6. `bucket/GhostWritingStyle.md` — Writing style rules
```

**Change to:**
```markdown
5. `bucket/NarrativeSpittoon.md` — Narrative framework rules (scene-level causality)
6. `bucket/GhostWritingStyle.md` — Writing mechanics rules (dialogue, pacing, voice)
7. `bucket/GhostWritingStyle-sentence.md` — Sentence-level prose style (parataxis, no literal but/because/therefore)
```

Renumber subsequent items (LoreBook becomes 8, JSON/mermaid becomes 9).

#### 4b. Update page generation rules (lines 88-89)

**Current:**
```markdown
   - Applies NarrativeSpittoon.md framework (implicit causality, subtle conflict, organic consequences)
   - Follows GhostWritingStyle.md rules (varied sentences, natural dialogue, etc.)
```

**Change to:**
```markdown
   - Applies NarrativeSpittoon.md framework (scene-level: implicit causality, subtle conflict, organic consequences — each beat earns the next through but/because/therefore reasoning)
   - Follows GhostWritingStyle.md rules (writing mechanics: varied sentences, natural dialogue, pacing)
   - Applies GhostWritingStyle-sentence.md rules (sentence-level: avoid literal but/because/therefore words — use parataxis, short declaratives, additive structure)
```

---

### Step 5: Update `commands/nsi4-refine.md`

**File:** `commands/nsi4-refine.md`

#### 5a. Update smoothing pass (line 75)

**Current:**
```markdown
4. Confirm causal connections are implicit (per NarrativeSpittoon.md)
```

**Change to:**
```markdown
4. Confirm causal connections are implicit at scene level (per NarrativeSpittoon.md) while sentence-level prose avoids literal but/because/therefore words (per GhostWritingStyle-sentence.md)
```

#### 5b. Update environment pass (line 83)

**Current:**
```markdown
3. Balance per GhostWritingStyle.md (don't slow pacing)
```

**Change to:**
```markdown
3. Balance per GhostWritingStyle.md (don't slow pacing) and GhostWritingStyle-sentence.md (maintain paratactic prose style)
```

---

### Step 6: Update `hooks/hooks.json`

**File:** `hooks/hooks.json`

#### 6a. Add `GhostWritingStyle-sentence.md` to Write hook protection (line 9)

**Current** (inside the prompt string):
```
bucket/NarrativeSpittoon.md, bucket/GhostWritingStyle.md, or bucket/HolographicTutor.md
```

**Change to** (in both occurrences within the Write hook prompt):
```
bucket/NarrativeSpittoon.md, bucket/GhostWritingStyle.md, bucket/GhostWritingStyle-sentence.md, or bucket/HolographicTutor.md
```

#### 6b. Add `GhostWritingStyle-sentence.md` to Edit hook protection (line 18)

**Current** (inside the prompt string):
```
bucket/NarrativeSpittoon.md, bucket/GhostWritingStyle.md, or bucket/HolographicTutor.md
```

**Change to:**
```
bucket/NarrativeSpittoon.md, bucket/GhostWritingStyle.md, bucket/GhostWritingStyle-sentence.md, or bucket/HolographicTutor.md
```

---

### Step 7: Update `agents/bucket-builder.md`

**File:** `agents/bucket-builder.md`

#### 7a. Add to protected files list (lines 142-147)

**Current:**
```markdown
- `bucket/NarrativeSpittoon.md`
- `bucket/GhostWritingStyle.md`
- `bucket/HolographicTutor.md`
```

**Change to:**
```markdown
- `bucket/NarrativeSpittoon.md`
- `bucket/GhostWritingStyle.md`
- `bucket/GhostWritingStyle-sentence.md`
- `bucket/HolographicTutor.md`
```

---

### Step 8: Update `skills/nsi4-workflow/SKILL.md`

**File:** `skills/nsi4-workflow/SKILL.md`

#### 8a. Update Phase 3 description (lines 48-51)

**Current:**
```markdown
1. **NarrativeSpittoon.md** — Implicit causality, subtle conflict, organic consequences (eliminates "because/but/therefore")
2. **GhostWritingStyle.md** — Sentence variation, natural dialogue, active voice, pacing
```

**Change to:**
```markdown
1. **NarrativeSpittoon.md** — Scene-level causality: implicit but/because/therefore reasoning that drives consequence chains between story beats
2. **GhostWritingStyle.md** — Writing mechanics: sentence variation, natural dialogue, active voice, pacing (overridable via --ghost)
3. **GhostWritingStyle-sentence.md** — Sentence-level prose style: avoid literal but/because/therefore words in prose — use parataxis, short declaratives, additive sentence structure
```

#### 8b. Update "Install three cognitive frameworks" to "Install four cognitive frameworks" (line 48)

**Current:**
```markdown
Install three cognitive frameworks that guide AI generation quality:
```

**Change to:**
```markdown
Install four cognitive frameworks that guide AI generation quality:
```

#### 8c. Update page generation requirements (line 65)

**Current:**
```markdown
- Follow GhostWritingStyle rules
```

**Change to:**
```markdown
- Follow GhostWritingStyle rules (mechanics) and GhostWritingStyle-sentence rules (prose style)
```

#### 8d. Update Required Bucket Files section (lines 104-106)

Add:
```markdown
- `GhostWritingStyle-sentence.md` — Sentence-level prose style
```

#### 8e. Update Three Cognitive Frameworks section header (line 114)

**Current:**
```markdown
## Three Cognitive Frameworks
```

**Change to:**
```markdown
## Four Cognitive Frameworks
```

#### 8f. Add new framework description (after line 129)

Add a new subsection after GhostWritingStyle:

```markdown
### GhostWritingSentenceStyle (Sentence-Level Prose)
- Avoid literal "but", "because", "therefore" as sentence connectors
- Use parataxis: short declarative chains without causal conjunctions
- Additive rather than causal sentence structure
- Vary sentence length: short for impact, medium for flow, long for atmosphere
- Mix structures: simple, compound, complex, fragment
- Active voice constructions preferred
- Specific over generic nouns and verbs
- Fresh metaphors used sparingly
- Cut unnecessary words and filter verbs
- Revision checklist for prose polish

**Relationship to NarrativeSpittoon**: NarrativeSpittoon drives scene-level "but/because/therefore" — the structural reasoning that makes each beat earn the next. GhostWritingSentenceStyle removes those same words from the actual prose, creating a clipped, accumulative register that performs meaning through omission rather than declaration.
```

---

### Step 9: Update Reference Files

#### 9a. `skills/nsi4-workflow/references/cognitive-frameworks.md`

**File:** `skills/nsi4-workflow/references/cognitive-frameworks.md`

Update "Overview" (line 5):
```markdown
The four cognitive frameworks are the core instruction modules that guide AI narrative
generation quality, style, and assessment.
```

Add new section after Framework 2 (after line 54):

```markdown
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
```

#### 9b. `skills/nsi4-workflow/references/refinement-passes.md`

**File:** `skills/nsi4-workflow/references/refinement-passes.md`

Update Pass 1 focus areas (line 32):
```markdown
- Adherence to GhostWritingStyle.md guidelines and GhostWritingStyle-sentence.md prose register
```

Update Pass 5 process item 5 (line 96):
```markdown
5. Balance description with action (per GhostWritingStyle.md) using paratactic prose (per GhostWritingStyle-sentence.md)
```

---

### Step 10: Update Documentation Files

#### 10a. `CLAUDE.md`

**File:** `CLAUDE.md`

Update the Architecture section to mention the fourth CORE file:

**Current:**
```markdown
- Three CORE cognitive frameworks (NarrativeSpittoon.md, GhostWritingStyle.md, HolographicTutor.md) are copied via literal `cp`
```

**Change to:**
```markdown
- Four CORE cognitive frameworks (NarrativeSpittoon.md, GhostWritingStyle.md, GhostWritingStyle-sentence.md, HolographicTutor.md) are copied via literal `cp` to prevent LLM paraphrase distortion
- GhostWritingStyle-sentence.md controls sentence-level prose style (parataxis, no literal but/because/therefore) and is always installed — not overridable by --ghost
```

#### 10b. `README.md`

**File:** `README.md`

**Phase 3 section (lines 123-144)** — Add after GhostWritingStyle description:

```markdown
**GhostWritingStyle-sentence.md** — Controls sentence-level prose register:
- Avoids literal "but/because/therefore" as prose connectors
- Uses parataxis, short declarative chains, additive structure
- Creates the clipped, accumulative prose style that performs meaning through omission
- Always installed from plugin source — not overridable via `--ghost`
- Works in combination with GhostWritingStyle.md (mechanics) and NarrativeSpittoon.md (scene causality)
```

Update "All three CORE files" to "All four CORE files" (line 144).

**Project Structure section (lines 261-305)** — Add to bucket/ listing:

```
│   ├── GhostWritingStyle-sentence.md  # CORE — copied verbatim via cp (sentence-level prose)
```

**Story Project Structure section (lines 324-348)** — Add to bucket/ listing:

```
│   ├── GhostWritingStyle-sentence.md  ← CORE: copied by /nsi4-start (immutable, always from plugin source)
```

#### 10c. `bucket-core-template-plan.md` (if it exists)

Add `GhostWritingStyle-sentence.md` to the CORE files list and note that it has no custom override mechanism unlike `GhostWritingStyle.md`.

---

### Step 11: Update NSL Converter for New CORE File

**File:** `scripts/nsl-converter.py`

The NSL converter must recognize `GhostWritingStyle-sentence.md` as a CORE framework file for export/import.

**Action:** Search the converter for where CORE files are listed and add the new file. Typically this is in a list or dict that maps bucket filenames to NSL XML element names.

The expected NSL element name: `<GhostWritingSentenceStyle>` (matching the tag wrapper in the file).

---

### Step 12: Update `commands/nsi4-export.md`

**File:** `commands/nsi4-export.md`

If the export command references CORE files by name (for special handling during export/import), add `GhostWritingStyle-sentence.md` to those lists.

---

## Implementation Order

Execute the steps in this sequence to minimize risk:

| Order | Step | Files Modified | Risk |
|:---:|:---:|---|---|
| 1 | Step 1 | `bucket/GhostWritingStyle-sentence.md` | Low — new file creation |
| 2 | Step 6 | `hooks/hooks.json` | Medium — enables protection before file exists in projects |
| 3 | Step 2 | `commands/nsi4-start.md` | Medium — core copy logic |
| 4 | Step 3 | `commands/nsi4-frameworks.md` | Low — verification logic |
| 5 | Step 4 | `commands/nsi4-generate.md` | Medium — generation context |
| 6 | Step 5 | `commands/nsi4-refine.md` | Low — refinement references |
| 7 | Step 7 | `agents/bucket-builder.md` | Low — protected files list |
| 8 | Step 8 | `skills/nsi4-workflow/SKILL.md` | Low — documentation |
| 9 | Step 9 | `references/*.md` | Low — documentation |
| 10 | Step 10 | `CLAUDE.md`, `README.md` | Low — documentation |
| 11 | Steps 11-12 | `scripts/nsl-converter.py`, `commands/nsi4-export.md` | Medium — serialization |

---

## Validation Checklist

After implementation, verify:

- [ ] `bucket/GhostWritingStyle-sentence.md` exists with `<GhostWritingSentenceStyle>` tags
- [ ] `/nsi4-start test-project` copies all 4 CORE files and passes diff verification
- [ ] `/nsi4-start test-project --ghost custom.md` copies the custom ghost AND GhostWritingStyle-sentence.md from plugin source
- [ ] Hooks block Write and Edit on `bucket/GhostWritingStyle-sentence.md`
- [ ] `/nsi4-frameworks` detects missing GhostWritingStyle-sentence.md and restores it
- [ ] `/nsi4-frameworks` does NOT overwrite an existing GhostWritingStyle-sentence.md
- [ ] `/nsi4-generate` reads GhostWritingStyle-sentence.md as part of pre-generation context
- [ ] `/nsi4-refine smoothing` checks sentence-level prose compliance
- [ ] `/nsi4-refine environment` respects paratactic prose style
- [ ] `/nsi4-export export` includes GhostWritingStyle-sentence.md in NSL output
- [ ] `/nsi4-export import` restores GhostWritingStyle-sentence.md from NSL input
- [ ] Bucket builder agent knows not to modify GhostWritingStyle-sentence.md
- [ ] All documentation references updated from "three" to "four" CORE frameworks
- [ ] SKILL.md accurately describes the two-layer but/because/therefore system

---

## Edge Cases

### User has `--ghost` custom file
The custom ghost overrides `GhostWritingStyle.md` (writing mechanics) only. `GhostWritingStyle-sentence.md` is always installed from the plugin source. Both files are active during generation. The custom ghost's mechanics rules combine with the sentence-style rules — no conflict, as they operate at different levels.

### User's custom ghost contains sentence-level rules
If a user's custom `--ghost` file includes its own sentence construction rules, those coexist with `GhostWritingStyle-sentence.md`. The sentence file takes precedence for but/because/therefore avoidance specifically. Documentation should note this in the Custom GhostWritingStyle section of README.md.

### Existing projects without `GhostWritingStyle-sentence.md`
When `/nsi4-frameworks` runs on a project created before this update, it will detect the missing file and restore it from the plugin source. No manual intervention required.

### NSL import of pre-update `.nsl` files
If an imported `.nsl` file does not contain a `<GhostWritingSentenceStyle>` element, `/nsi4-export import` should install the default from the plugin source (same as the missing-file restoration logic).

---

## Summary

This implementation adds a fourth CORE cognitive framework that codifies the emergent prose benefit discovered through the accidental inversion — the clipped, paratactic sentence style — while keeping it separate from the scene-level causality system. The result: structurally rigorous plots scored through but/because/therefore reasoning (NarrativeSpittoon.md), rendered in prose that withholds those same causal words at the sentence level (GhostWritingStyle-sentence.md), with configurable writing mechanics (GhostWritingStyle.md via `--ghost`).

Thirteen files modified. One new file created. Zero breaking changes to existing projects.
