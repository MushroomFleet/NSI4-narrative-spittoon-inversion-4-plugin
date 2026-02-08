---
description: Convert between bucket folder and NSL 1.1 XML format
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - AskUserQuestion
argument-hint: "[export|import] [path]"
---

## Context

You are executing NSL 1.1 format conversion.

Bucket contents: !`ls bucket/ 2>/dev/null || echo "No bucket found"`
Story pages: !`ls STORY/ 2>/dev/null || echo "No story pages found"`
Python available: !`python3 --version 2>/dev/null || python --version 2>/dev/null || echo "Python not found"`

## Your Task

Convert between the bucket folder structure and NSL 1.1 XML format.

### Export (bucket to .nsl)

If first argument is "export" or no argument:

1. Verify bucket/ and STORY/ directories exist
2. Run the NSL converter script:
   ```
   python3 ${CLAUDE_PLUGIN_ROOT}/scripts/nsl-converter.py export --bucket ./bucket --story ./STORY --output [project-name].nsl
   ```
3. If no output path specified, use the project directory name + `.nsl`
4. Report the generated file path and size

### Import (.nsl to bucket)

If first argument is "import":

1. The second argument should be the path to an `.nsl` file
2. Ask user if they want to overwrite existing bucket/ contents (if any)
3. Run the NSL converter script:
   ```
   python3 ${CLAUDE_PLUGIN_ROOT}/scripts/nsl-converter.py import --input [path.nsl] --bucket ./bucket --story ./STORY
   ```
4. **Check the output for CONTENT WARNINGS.** The converter validates that imported story pages contain real content rather than placeholder text. If warnings appear:
   - Tell the user which pages have placeholder/abbreviated content
   - Explain that the source NSL file did not contain complete story text
   - The story pages need to be written or provided separately
5. After import, read each `STORY/page*.md` file and verify it contains substantial prose (800-1500 words expected per page). Pages with under 100 words or containing `[Content continues` or `[Full content` markers are incomplete.
6. Report what was extracted and created, including any content warnings

### If Python is not available:

Inform the user that the NSL converter requires Python 3.6+. Offer to:
1. Perform a manual XML export by reading all bucket files and constructing the NSL XML inline
2. Skip the conversion

### Error Handling

- If bucket is empty: "No bucket files to export. Run /nsi4-interview and /nsi4-bucket first."
- If .nsl file not found: "File not found: [path]. Please provide a valid .nsl file path."
- If Python errors: Show error output and suggest fixes
