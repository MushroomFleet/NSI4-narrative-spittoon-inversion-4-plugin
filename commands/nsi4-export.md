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
4. Report what was extracted and created

### If Python is not available:

Inform the user that the NSL converter requires Python 3.6+. Offer to:
1. Perform a manual XML export by reading all bucket files and constructing the NSL XML inline
2. Skip the conversion

### Error Handling

- If bucket is empty: "No bucket files to export. Run /nsi4-interview and /nsi4-bucket first."
- If .nsl file not found: "File not found: [path]. Please provide a valid .nsl file path."
- If Python errors: Show error output and suggest fixes
