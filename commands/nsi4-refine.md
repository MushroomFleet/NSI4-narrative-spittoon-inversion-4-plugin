---
description: Run refinement passes on the completed story (quality assessment, speech style, repetition, smoothing, environment)
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Task
  - AskUserQuestion
argument-hint: "[score|speech|repetition|smoothing|environment|all]"
---

## Context

You are executing NSI4 Phase 5: Refinement.

Story pages: !`ls -la STORY/page*.md 2>/dev/null || echo "ERROR: No story pages found. Run /nsi4-generate first."`
Bucket status: !`ls bucket/project-instructions.md 2>/dev/null || echo "No manifest found"`

## Your Task

Run the specified refinement pass on the completed story. If no argument, show available passes and ask which to run.

### Available Passes

| Pass | Argument | Description |
|------|----------|-------------|
| Quality Assessment | `score` | Score each page 0-100 using HolographicTutor |
| Speech Style | `speech` | Verify character voice consistency |
| Repetition Sniper | `repetition` | Eliminate redundant phrasing |
| Narrative Smoothing | `smoothing` | Polish transitions and foreshadowing |
| Environmental Enhancement | `environment` | Deepen sensory details |
| All Passes | `all` | Run all passes in recommended order |

### If no argument provided:

Use AskUserQuestion to ask which pass to run, showing descriptions for each option.

### Pass Execution

#### Score Pass
Use the holographic-tutor agent (via Task tool) to evaluate each page:
1. Read each page (page0 through page5)
2. Read bucket/HolographicTutor.md for the assessment framework
3. For each page, apply the Score function: numerical score /100 with justification
4. Present results as a summary table
5. Identify the weakest pages and recommend targeted improvement

#### Speech Pass
For all dialogue across all pages:
1. Read bucket/speechstyles.md for character speech definitions
2. Read each story page
3. For each character's dialogue, verify:
   - Adherence to defined speech style
   - Consistent vocabulary and sentence structure
   - Verbal tics present and consistent
   - Natural pauses and filler words
4. Update pages with refined dialogue (maintaining story beats)
5. Show a diff summary of changes

#### Repetition Pass
Scan all pages for redundancy:
1. Read all story pages
2. Identify: similar sentence structures, repeated phrases, overused words, redundant descriptions, duplicated character beats
3. For each instance, report: the element (first 5 words), which pages, suggested alternative
4. After presenting findings, ask user which to fix
5. Apply approved fixes

#### Smoothing Pass
Polish transitions and continuity:
1. Read all pages in forward order (page0 through page5)
2. Check page-to-page flow (reverse-generation seams)
3. Verify foreshadowing in earlier pages pays off
4. Confirm causal connections are implicit (per NarrativeSpittoon.md)
5. Polish scene transitions within pages
6. Update pages with improvements

#### Environment Pass
Enhance sensory atmosphere:
1. Read all pages and bucket/world.md
2. For each page, add: vivid sensory descriptions, deepened atmosphere, environment reflecting character emotions, world-building details
3. Balance per GhostWritingStyle.md (don't slow pacing)
4. Update pages with enriched detail

### After Any Pass

Report what was changed and suggest the next recommended pass.
