---
name: yt-package
description: Improve YouTube title and thumbnail copy as one coordinated package. Use when naming a video, reviewing thumbnail text, or checking whether the click promise is clear and non-misleading.
---

# CreatorPilot: Title + Thumbnail Package

## Workflow
1. Identify the intended viewer, topic, and truthful payoff.
2. Offer 5 title options with different angles; avoid false urgency and unsupported claims.
3. Suggest 3 concise thumbnail-text options, or explain when no text may be better.
4. Ensure title and thumbnail complement each other instead of repeating the same phrase.
5. Run the local lint tool if available:
   `python tools/creatorpilot.py title "TITLE" --thumbnail "THUMBNAIL TEXT"`
6. Explain each warning in plain language. Heuristics are prompts for review, not rules from YouTube.
7. Recommend one package and state the audience/promise it communicates.
8. Do not claim predicted CTR or virality without valid experiment data.

## Output
- Target viewer and promise
- Title options
- Thumbnail text options
- Overlap/clarity review
- Recommended pairing and rationale
