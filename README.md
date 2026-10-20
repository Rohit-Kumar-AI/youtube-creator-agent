# YouTube Creator Agent 🚀

**Open-source YouTube AI agent skills for Claude Code and OpenAI Codex.**

Turn your creator workflow into reusable AI-assisted tasks: brainstorm video ideas, write stronger hooks and scripts, improve title–thumbnail combinations, and discover potential YouTube Shorts from timestamped transcripts.

**CreatorPilot AI** provides shared agent instructions and lightweight Python tools you can run locally — without API keys, paid services, or third-party Python dependencies.

[Features](#features) · [Quick Start](#quick-start) · [Install Skills](#install-skills) · [Examples](#examples) · [Contributing](CONTRIBUTING.md)

## Why CreatorPilot AI?

- **One shared workflow:** reusable skills designed for Claude Code and Codex.
- **Local Python utilities:** inspect hooks, check title and thumbnail text, and rank transcript clip candidates.
- **Transparent heuristics:** understand why a tool flags text instead of trusting an unexplained AI score.
- **No API keys required:** the included Python utilities work offline with Python 3.10+.
- **Human-directed creation:** use the results as creative suggestions, then review and edit before publishing.

## Features

| Tool or skill | What it helps with |
|---|---|
| Hook checker | Evaluate opening lines for clarity, specificity, curiosity, and concision |
| Title checker | Flag vague or long titles, all-caps text, and repeated title/thumbnail wording |
| Transcript clip finder | Rank candidate Shorts moments from timestamped text |
| `yt-script` | Plan video scripts and stronger openings |
| `yt-package` | Develop complementary titles and thumbnail text |
| `yt-shorts` | Turn transcript highlights into candidate short-form clips |

> **Important:** The Python utilities use rule-based heuristics, not predictive AI models. They cannot guarantee views, retention, rankings, or virality.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Rohit-Kumar-AI/youtube-creator-agent.git
cd youtube-creator-agent
```

### 2. Run the tests

```bash
python -m unittest discover -s tests -v
```

### 3. Check a video hook

```bash
python tools/creatorpilot.py hook "I wasted 30 days learning Python the wrong way."
```

### 4. Check a title and thumbnail phrase

```bash
python tools/creatorpilot.py title "I learned Python in 30 days" --thumbnail "30 days"
```

### 5. Find candidate Shorts moments

```bash
python tools/creatorpilot.py clips examples/sample_transcript.txt
```

No external Python packages are required for these commands.

## Install Skills

The `skills/` directory contains reusable `SKILL.md` instructions.

- **Claude Code:** copy the skill directories into `~/.claude/skills/`.
- **OpenAI Codex:** copy them into `~/.codex/skills/` if supported by your installed version.

See the installation instructions below for the exact commands. Agent discovery behavior can vary by version, so verify the supported skill path for your setup.

## Project Structure

```text
youtube-creator-agent/
├── skills/
│   ├── yt-script/
│   ├── yt-package/
│   └── yt-shorts/
├── tools/
│   └── creatorpilot.py
├── tests/
├── examples/
├── docs/
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Design Principles

- Useful without API keys or paid services.
- Transparent, testable local utilities.
- Reusable instructions across supported coding agents.
- No automatic publishing or hidden network activity.
- Human review before publishing creator content.

## Roadmap

- [x] Hook-scoring heuristic
- [x] Title and thumbnail text checks
- [x] Timestamped transcript clip suggestions
- [x] Shared agent skill instructions
- [x] Unit tests and sample transcript
- [ ] YouTube Analytics CSV analysis
- [ ] Improved multilingual and Hinglish support
- [ ] Continuous integration and release automation

## Contributing

Contributions are welcome! Add test cases, improve feedback, document new workflows, or help expand language support. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the MIT License. See [LICENSE](LICENSE).

---

**Built for creators and developers who want practical, reusable YouTube workflows.**
