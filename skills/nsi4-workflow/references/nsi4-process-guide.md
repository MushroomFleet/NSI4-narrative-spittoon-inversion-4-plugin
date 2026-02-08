# NSI4 Process Guide — Quick Reference

## Complete Workflow at a Glance

```
/nsi4-start [project-name]
    Creates bucket/ and STORY/ folders
    Copies template files into bucket/

/nsi4-interview
    Runs 20-question dynamic interview
    Builds bucket/LoreBook.md incrementally
    Covers: universe, characters, plot, themes, tone, ending

/nsi4-bucket
    Reads LoreBook.md
    Generates: world.md, characters.md, speechstyles.md
    Generates: glossary, technical specs (.json), diagrams (.mermaid)
    Uses bucket-builder agent for structured creation

/nsi4-frameworks
    Installs NarrativeSpittoon.md, GhostWritingStyle.md, HolographicTutor.md
    Generates project-instructions.md manifest
    Validates all bucket files present

/nsi4-generate
    Reads all bucket files for context
    Creates or gets approval for Page 5 (ending)
    Generates Page 4, 3, 2, 1, 0 with approval gates
    Applies Hero's Journey mapping per page
    Writes each page to STORY/pageN.md

/nsi4-refine [pass-name]
    Runs selected refinement pass
    Available: score, speech, repetition, smoothing, environment, all
    Uses holographic-tutor agent for assessment

/nsi4-export [import|export] [path]
    export: bucket/ folder to .nsl XML file
    import: .nsl XML file to bucket/ folder
    Uses nsl-converter.py script
```

## Validation Checkpoints

### After Phase 1 (Interview)
- [ ] LoreBook.md exists in bucket/
- [ ] Contains 20 questions and answers
- [ ] World setting clearly described
- [ ] Main characters defined
- [ ] Story ending specified
- [ ] Tone and themes established

### After Phase 2 (Bucket)
- [ ] world.md captures essential setting
- [ ] All main characters documented in characters.md
- [ ] Each character has distinct speech style in speechstyles.md
- [ ] At least one technical spec or diagram created
- [ ] Glossary covers universe-specific terminology

### After Phase 3 (Frameworks)
- [ ] All three cognitive framework files present
- [ ] project-instructions.md lists all bucket contents
- [ ] Each file has description in manifest

### After Phase 4 (Generation)
- [ ] All 6 pages exist (page0.md through page5.md)
- [ ] Pages flow naturally in forward chronological order
- [ ] Character voices consistent
- [ ] World-building cohesive
- [ ] Hero's Journey structure apparent
- [ ] Story feels complete and purposeful

### After Phase 5 (Refinement)
- [ ] Selected passes completed
- [ ] Quality score improved
- [ ] Character voices consistent across pages
- [ ] No excessive repetition
- [ ] Transitions smooth
- [ ] Sensory detail appropriate

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| AI forgets context | Re-read bucket/project-instructions.md |
| Character voice drift | Reference speechstyles.md explicitly |
| Plot holes | Read forward (page0 to page5) and note gaps |
| Pages too short/long | Specify target word count (800-1500) |
| Ending doesn't work | Revise page5 before continuing backward |
| World inconsistencies | Cross-check against world.md |
| Framework not applied | Explicitly cite framework rules |
