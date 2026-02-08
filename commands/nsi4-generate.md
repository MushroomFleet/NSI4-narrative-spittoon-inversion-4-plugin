---
description: Generate the story in reverse chronological order (Page 5 to Page 0) with approval gates
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
argument-hint: "[page-number]"
---

## Context

You are executing NSI4 Phase 4: Story Generation — The Inversion.

Project manifest: !`cat bucket/project-instructions.md 2>/dev/null || echo "ERROR: No manifest. Run /nsi4-frameworks first."`
Existing story pages: !`ls STORY/page*.md 2>/dev/null || echo "No pages yet"`

## Your Task

Generate the story in reverse chronological order. Each page is written backward from the ending, with user approval between each page.

### If page-number argument provided:
Generate only that specific page (e.g., `/nsi4-generate 3` generates page3.md only).

### If no argument:
Run the full reverse generation from the next unwritten page.

### Pre-Generation: Load All Context

Before generating ANY page, read these bucket files:
1. `bucket/project-instructions.md` — Component manifest
2. `bucket/world.md` — World-building context
3. `bucket/characters.md` — Character profiles
4. `bucket/speechstyles.md` — Speech patterns
5. `bucket/NarrativeSpittoon.md` — Narrative framework rules
6. `bucket/GhostWritingStyle.md` — Writing style rules
7. `bucket/LoreBook.md` — Original knowledge base
8. Any `.json` and `.mermaid` files in bucket/ for technical context

### Generation Order

**Page 5 (Ending)** then **Page 4** then **Page 3** then **Page 2** then **Page 1** then **Page 0 (Beginning)**

### For Page 5 (The Ending)

Ask the user via AskUserQuestion:
- "Would you like to write the ending yourself, or shall I generate it based on the LoreBook?"
- Options: "Generate it for me", "I'll write it myself", "I have a draft to refine"

If generating: Create a compelling final page that resolves the central conflict, shows character transformation, establishes tone, 800-1500 words.

If user writes: Wait for them to create STORY/page5.md, then read and confirm.

After page5 exists, ask for approval before continuing.

### For Pages 4 through 0

For each page, follow this process:

1. **Read the next page** (chronologically — the page that follows this one in the story):
   - When writing page4, read page5
   - When writing page3, read page4 AND page5
   - When writing page2, read pages 3, 4, 5
   - When writing page1, read pages 2, 3, 4, 5
   - When writing page0, read ALL other pages

2. **Identify the Hero's Journey stage** for this page:
   | Page | Stage | Function |
   |------|-------|----------|
   | 5 | Return with Elixir / Resolution | Conclusion |
   | 4 | Resurrection / Climax | Ultimate test |
   | 3 | Road Back / Rising Action | Stakes escalate |
   | 2 | Ordeal / Commitment | Point of no return |
   | 1 | Tests, Allies, Enemies / Setup | World establishment |
   | 0 | Ordinary World / Opening | Beginning |

3. **Generate the page** (800-1500 words) ensuring:
   - Answers "what led to the next page's events?"
   - Maintains character consistency (reference speechstyles.md)
   - Builds world details (reference world.md)
   - Applies NarrativeSpittoon.md framework (implicit causality, subtle conflict, organic consequences)
   - Follows GhostWritingStyle.md rules (varied sentences, natural dialogue, etc.)
   - Uses the Hero's Journey stage for this page number
   - Flows naturally into the next page

4. **Write to STORY/page[N].md**

5. **Present the page** to the user and ask for approval via AskUserQuestion:
   - "Page [N] generated ([word count] words). Approve or request revisions?"
   - Options: "Approved — continue to next page", "Needs revisions", "Let me review and I'll respond"

6. **If revisions requested**: Ask what to change, revise, and re-present for approval.

7. **After approval**: Continue to the next page (N-1).

### After All Pages Complete

1. List all 6 pages with word counts
2. Suggest reading the story forward (page0 through page5)
3. Suggest running `/nsi4-refine` for quality assessment

### Page Format

Each page file should contain:

```markdown
# Page [N]: [Brief Title]

[Story content — 800-1500 words]

---
*Hero's Journey Stage: [Stage Name]*
*Word Count: [count]*
*Generation Order: [which number this was generated]*
```
