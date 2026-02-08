# NSI4 Refinement Passes

## Overview

Phase 5 refinement passes polish a completed draft. Apply them in order, one at a time,
reviewing changes before proceeding to the next pass.

## Recommended Order

1. Quality Assessment (identify issues first)
2. Speech Style Pass (character consistency)
3. Repetition Sniper (eliminate redundancy)
4. Narrative Smoothing (polish flow)
5. Environmental Enhancement (deepen atmosphere)
6. Final Quality Assessment (confirm improvements)

---

## Pass 1: Quality Assessment

**Tool**: HolographicTutor agent — Score function

**Process**: For each page (page0.md through page5.md):
1. Score the page (0-100)
2. Identify specific areas for improvement
3. Note inconsistencies with other pages

**Focus areas**:
- Plot coherence across the reverse-generated structure
- Character voice consistency
- Pacing and flow
- Adherence to GhostWritingStyle.md guidelines

---

## Pass 2: Speech Style Pass

**Purpose**: Enhance character voice consistency across all pages.

**Process**: For each character's dialogue across all pages:
1. Verify adherence to their style in speechstyles.md
2. Ensure consistent vocabulary, sentence structure, verbal tics
3. Make dialogue natural while maintaining distinctiveness
4. Add/adjust pauses, filler words, emotional indicators

**Common issues**:
- Characters sounding too similar
- Vocabulary level shifting between pages
- Missing verbal tics established in speechstyles.md
- Emotional expression inconsistency

---

## Pass 3: Repetition Sniper

**Purpose**: Eliminate redundant phrasing and descriptions.

**Scan targets**:
1. Similar sentence structures used excessively
2. Repeated descriptive phrases
3. Overused words or expressions
4. Redundant scene descriptions
5. Duplicated character beats

**Output format** (per instance):
- The repetitive element (first 5 words)
- Which pages it appears in
- Suggested alternative

---

## Pass 4: Narrative Smoothing

**Purpose**: Polish transitions between pages and scenes.

**Process**:
1. Ensure smooth flow from page to page (remember reverse generation order)
2. Check that foreshadowing in earlier pages pays off appropriately
3. Verify causal connections are clear but not explicit (per NarrativeSpittoon.md)
4. Polish scene transitions within pages
5. Enhance pacing in slow sections

**Key concern**: Pages written in reverse may have subtle discontinuities when read forward. This pass specifically targets those seams.

---

## Pass 5: Environmental Enhancement

**Purpose**: Deepen sensory details and atmosphere.

**Process**: For each page:
1. Add vivid sensory descriptions (sight, sound, smell, touch, taste)
2. Deepen atmosphere and mood
3. Use environment to reflect character emotions
4. Integrate world-building details naturally (reference world.md)
5. Balance description with action (per GhostWritingStyle.md)

**Warning**: Do not slow pacing. Environmental details should enhance, not pad.
