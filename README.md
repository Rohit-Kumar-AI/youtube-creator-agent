# YouTube Creator Agent — CreatorPilot AI

**A shared YouTube creator workflow for Claude Code and OpenAI Codex.** Create stronger scripts, improve title/thumbnail packaging, and identify Shorts opportunities with lightweight local Python tools.

> Independent open-source project. Inspired by the broader ecosystem of YouTube creator agent skills; not affiliated with or a copy of any similarly named project.

**GitHub repository:** `Rohit-Kumar-AI/youtube-creator-agent`

**Suggested GitHub topics:** `youtube-agent`, `youtube-agent-skills`, `claude-code`, `codex`, `ai-agents`, `youtube-automation`, `creator-tools`, `python`


## What’s included

| Feature | What it does | Command |
|---|---|---|
| Hook checker | Scores a video opening against explainable signals: clarity, specificity, tension, and concision | `python tools/creatorpilot.py hook "Most people make this mistake..."` |
| Title checker | Flags vague/long titles, all-caps, repeated title/thumbnail wording, and missing concrete language | `python tools/creatorpilot.py title "Stop making these Python mistakes" --thumbnail "Python mistakes"` |
| Transcript moments | Finds timestamped transcript segments and ranks candidate clips using simple signals | `python tools/creatorpilot.py clips examples/sample_transcript.txt` |
| Agent workflows | Reusable instructions for script planning, packaging, and transcript-to-Shorts workflows | `skills/` |

## Quick start

Requirements: Python 3.10+ and Git. No third-party Python packages are required.

```bash
git clone https://github.com/Rohit-Kumar-AI/youtube-creator-agent.git
cd youtube-creator-agent

# Run the tests
python -m unittest discover -s tests -v

# Check a hook
python tools/creatorpilot.py hook "I wasted 30 days learning Python the wrong way."

# Check a title and thumbnail phrase together
python tools/creatorpilot.py title "I learned Python in 30 days" --thumbnail "30 days"

# Find candidate moments from a timestamped transcript
python tools/creatorpilot.py clips examples/sample_transcript.txt
```

If your GitHub username or repository name differs, update the clone URL above.

## Install skills

The `SKILL.md` files follow the portable Agent Skills format. Agent discovery paths can differ by tool/version, so install the same skill directories into the appropriate folder.

### Claude Code (user-level)

macOS/Linux/Git Bash:
```bash
mkdir -p ~/.claude/skills
cp -R skills/yt-script skills/yt-package skills/yt-shorts ~/.claude/skills/
```

### OpenAI Codex (user-level)

macOS/Linux/Git Bash:
```bash
mkdir -p ~/.codex/skills
cp -R skills/yt-script skills/yt-package skills/yt-shorts ~/.codex/skills/
```

Restart the agent after installing if it does not discover the new skills. For a project-only install, use the corresponding `.claude/skills/` or `.codex/skills/` directory in your project. Confirm the supported discovery path in the documentation for your installed version.

## Example workflow

1. Draft a rough idea and audience promise.
2. Use `yt-script` to explore several opening approaches and a script outline.
3. Use `yt-package` to make title and thumbnail copy complement rather than repeat each other.
4. Use `yt-shorts` to identify candidate moments from a timestamped transcript.
5. Run the relevant local checks and revise manually.
6. Publish only after human review.

## How scores work

- **Hook score (0–100):** transparent rule-based signals, not an ML model. It rewards concrete details, a clear audience/problem, curiosity/tension, and brevity. A score cannot establish likely views or retention.
- **Title checks:** lightweight text heuristics. They do not measure search volume, audience fit, or thumbnail image quality.
- **Clip ranking:** ranks timestamped segments using text cues and duration. It does not inspect video/audio and does not produce edited media.

## Example output

```text
Hook score: 72/100
Signals:
  + Has a concrete detail
  + Contains a curiosity/tension cue
  - Could identify the audience more clearly
Advice:
  Make the audience and promised outcome more explicit.
```

Exact scores depend on the input and version; use the tools as a checklist, not a verdict.

## Roadmap

- [x] Dependency-free hook heuristic
- [x] Title/thumbnail text linting
- [x] Timestamped transcript moment suggestions
- [x] Shared Claude Code / Codex skill content
- [x] Unit tests and sample input
- [ ] Optional YouTube Analytics CSV import
- [ ] More language-aware heuristics (including Hinglish)
- [ ] CI workflow and release automation

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Good first contributions include additional test cases, clearer feedback, localization, and documented examples.

## Safety and privacy

- Tools process only the text/files you pass to them.
- No network requests, telemetry, credentials, or automatic publishing.
- Review generated copy and respect copyright, privacy, platform policies, and the rights of people in any source material.

## License

MIT — see [LICENSE](LICENSE).
