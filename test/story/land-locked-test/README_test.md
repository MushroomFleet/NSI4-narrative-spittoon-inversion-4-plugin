# NSI4 Plugin Test — Land Locked

Test run of the NSI4 plugin using an NSL 1.1 import and HolographicTutor scoring.

---

## Input Files

| File | Description |
|------|-------------|
| `land-locked.nsl` | NSL 1.1 archive of "Land Locked" — a Halloween horror story created with NSI 3.0 |
| `page5.md` | Full ending page (the first page written during reverse generation) |

## Test Prompt

```
NSL "land-locked.nsl"
final page "page5.md"
```

The converter imported the NSL into `land-locked-test/` and the full page5 was copied into `STORY/` replacing the abbreviated NSL version.

---

## Results

| Step | Status | Notes |
|------|--------|-------|
| NSL Import | Pass | 17 files extracted via `nsl-converter.py` |
| XML Fix | Minor | Unescaped `&` in `Q&A` (source file issue, not converter) |
| Bucket Structure | Pass | All artifacts created with correct tags |
| project-instructions.md | Pass | Auto-generated manifest indexes 11 bucket files |
| Story Pages | Pass | 6 pages created in `STORY/` (page0-page5) |
| HolographicTutor Score | Pass | **91/100** on page5 |

## Imported Structure

```
land-locked-test/
  bucket/
    NarrativeSpittoon.md
    GhostWritingStyle.md
    HolographicTutor.md
    world.md
    characters.md
    speechstyles.md
    hellmouth-mechanics.json
    character-relationships.mermaid
    lorebook.md
    quad-glossary.txt
    project-instructions.md
  STORY/
    page0.md - page5.md
```

## HolographicTutor Score — Page 5

**Score: 91/100**

**Strengths**: Strong atmospheric control, character voice consistency (Jane decisive, Matt anxious), effective ambiguity in the bystander character, sensory immersion throughout.

**Areas for Improvement**: Mid-page flashback slightly disrupts urgency, repeated "Couldn't tell" anaphora borders on overuse, bystander mystery flagging leans toward telling.
