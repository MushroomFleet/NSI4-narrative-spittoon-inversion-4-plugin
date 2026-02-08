---
description: Run the 20-question LoreBook interview to gather story knowledge
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
argument-hint: "[resume]"
---

## Context

You are conducting the NSI4 Knowledge Gathering interview (Phase 1).

Check for existing LoreBook: !`ls bucket/LoreBook.md 2>/dev/null || echo "No LoreBook found"`
Check for existing materials: !`ls bucket/*.md 2>/dev/null || echo "No bucket files found"`

## Your Task

Conduct a dynamic 20-question interview to build a comprehensive LoreBook. The LoreBook captures all essential story elements needed for the Narrative Spittoon Inversion process.

### If "resume" argument is provided:
Read the existing `bucket/LoreBook.md` and continue from where the interview left off.

### Interview Process

1. **Create `bucket/LoreBook.md`** with a header section:
   ```markdown
   # LoreBook: [Story Title TBD]

   ## Interview Progress
   Questions completed: 0/20
   Status: In Progress
   ```

2. **Ask questions one at a time** using AskUserQuestion. After each answer:
   - Append the Q&A pair to LoreBook.md
   - Update the question counter
   - Adapt the next question based on what has been revealed

3. **Question categories to cover** (dynamically ordered based on answers):
   - Questions 1-4: **Universe & Setting** — World, time period, physical laws, society
   - Questions 5-8: **Characters** — Main cast, personalities, motivations, relationships
   - Questions 9-12: **Story & Plot** — Central conflict, stakes, key events
   - Questions 13-15: **The Ending** — How the story concludes (critical for reverse generation)
   - Questions 16-18: **Tone & Themes** — Atmosphere, genre conventions, thematic depth
   - Questions 19-20: **Final Details** — Anything missing, special requirements

4. **Each question should**:
   - Build on previous answers
   - Probe deeper into mentioned but unexplored areas
   - Offer specific options when helpful (via AskUserQuestion options)
   - Never repeat information already captured

5. **After all 20 questions**, update LoreBook.md:
   - Set status to "Complete"
   - Add a summary section at the top
   - Suggest running `/nsi4-bucket` as the next step

### LoreBook Format

```markdown
# LoreBook: [Story Title]

## Summary
[Brief 2-3 paragraph summary of the story project]

## Interview Progress
Questions completed: 20/20
Status: Complete

---

## Q1: [Question text]
**A:** [User's answer]

## Q2: [Question text]
**A:** [User's answer]

[... through Q20]
```

### Important Rules

- Ask ONE question at a time — do not batch questions
- Write to LoreBook.md after EACH answer (incremental saves)
- The ending (Questions 13-15) is CRITICAL — probe thoroughly
- If user provides extensive materials upfront, adapt questions to fill gaps rather than repeat
- Keep questions specific and actionable, not vague
