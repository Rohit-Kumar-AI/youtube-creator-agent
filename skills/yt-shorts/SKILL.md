---
name: yt-shorts
description: Find candidate YouTube Shorts moments from a timestamped transcript and suggest a new opening line for each. Use when repurposing a long-form video or transcript into short vertical videos.
---

# CreatorPilot: Transcript to Shorts

## Workflow
1. Ask for a transcript with timestamps or locate the supplied transcript file. Never claim to analyze video or audio if only text is available.
2. If in the repository, run:
   `python tools/creatorpilot.py clips path/to/transcript.txt --limit 8`
3. Treat results as candidate moments only. Read surrounding context to ensure each clip makes sense independently and does not distort the speaker's meaning.
4. For each selected moment, propose a hook, a concise clip title, the core takeaway, and any context needed at the beginning.
5. Preserve the original meaning; mark any proposed cuts as suggestions.
6. Recommend human review of exact timestamps and copyright/privacy considerations before publishing.

## Output
- Candidate timestamp
- Why it may work as a standalone moment
- Suggested opening line
- Suggested title/caption
- Context or editing cautions
