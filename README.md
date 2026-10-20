# YouTube Creator Agent 🚀

**Open-source YouTube AI agent skills for Claude Code and OpenAI Codex.**

CreatorPilot AI helps creators and developers build repeatable YouTube workflows for video scripting, stronger hooks, title and thumbnail optimization, and YouTube Shorts discovery from timestamped transcripts.

It combines reusable agent instructions with lightweight Python tools that run locally — no API keys or third-party Python dependencies required for the included utilities.

[Features](#-features) · [Quick Start](#-quick-start) · [Usage Examples](#-usage-examples) · [Agent Skills](#-agent-skills) · [Testing](#-testing) · [Contributing](#-contributing)

---

## ✨ Why CreatorPilot AI?

- **Claude Code + Codex:** reusable skill instructions for supported coding agents.
- **YouTube creator workflows:** plan scripts, strengthen hooks, and brainstorm title–thumbnail combinations.
- **Local Python tools:** inspect hooks, check packaging text, and find candidate Shorts moments.
- **No API keys:** run the included utilities locally without paid APIs.
- **Transparent results:** rule-based checks provide suggestions, not unexplained promises of virality.
- **Open source:** inspect, customize, test, and contribute to the code.

## 🧰 Features

| Component | Purpose |
|---|---|
| Hook checker | Reviews opening lines using simple text heuristics |
| Title checker | Flags potential title and thumbnail wording issues |
| Transcript clip finder | Identifies timestamped moments worth reviewing for Shorts |
| `yt-script` skill | Helps plan and draft video scripts |
| `yt-package` skill | Helps brainstorm video titles and thumbnail text |
| `yt-shorts` skill | Helps turn transcript highlights into short-form video ideas |

**Important:** The Python tools use rule-based heuristics. They do not predict YouTube views, guarantee retention, or guarantee viral performance.

## 🚀 Quick Start

### Requirements

- Python 3.10 or newer
- Git (for cloning the repository)
- Claude Code or Codex if you want to use the agent skills

### 1. Clone the repository

```bash
git clone https://github.com/Rohit-Kumar-AI/youtube-creator-agent.git
cd youtube-creator-agent
```

### 2. Check the available commands

```bash
python tools/creatorpilot.py --help
```

On Windows, use `py` instead of `python` if that is how Python is installed.

### 3. Run the tests

```bash
python -m unittest discover -s tests -v
```

The included Python utilities are designed to run without installing external packages.

## 💡 Usage Examples

### Example 1: Review a video hook

Check an opening line before using it in a video.

```bash
python tools/creatorpilot.py hook "I wasted 30 days learning Python the wrong way."
```

**When to use it:** While drafting a coding tutorial, educational video, or personal learning story.

Review the tool's feedback and rewrite the hook where useful. A heuristic score is a guide, not a measure of guaranteed audience engagement.

### Example 2: Check a title and thumbnail phrase

```bash
python tools/creatorpilot.py title "I learned Python in 30 days" --thumbnail "30 days"
```

**When to use it:** Before publishing a video, check whether the title and thumbnail wording may be too long, vague, repetitive, or excessively capitalized.

The goal is to make the title and thumbnail complementary rather than simply repeating the same words.

### Example 3: Find potential Shorts moments

Run the clip finder against the sample transcript:

```bash
python tools/creatorpilot.py clips examples/sample_transcript.txt
```

A timestamped transcript might look like this:

```text
00:00:01 Introduction to Python
00:00:08 Most beginners make this mistake
00:00:18 Here is the simple fix
00:00:35 Let's test the solution
```

The tool can suggest timestamped candidate moments for further review. Check the actual transcript and video before choosing a clip.

### Example 4: Use a skill to draft a video script

Open `skills/yt-script/SKILL.md` and follow its instructions in your supported coding agent.

Example task to give your agent:

> Help me draft an 8-minute beginner-friendly YouTube video about common C++ mistakes. Start with three hook options, create a logical outline, and suggest examples for each section. Avoid unsupported claims.

### Example 5: Brainstorm titles and thumbnail text

Open `skills/yt-package/SKILL.md` and use it with a task such as:

> Suggest 10 accurate YouTube titles for my beginner Python tutorial. For the best three, propose short thumbnail text that complements the title rather than repeating it. Explain the intended audience and angle.

### Example 6: Plan Shorts from a transcript

Open `skills/yt-shorts/SKILL.md` and ask your agent:

> Review this timestamped transcript and identify potential Shorts segments. For each candidate, provide the start and end timestamps, the central idea, a possible opening line, and why it may work as a standalone clip. Do not invent timestamps or transcript content.

These prompts illustrate intended workflows. The Python CLI commands and agent skills are separate components.

## 🤖 Agent Skills

The `skills/` directory contains reusable `SKILL.md` instructions.

| Skill | Intended workflow |
|---|---|
| `yt-script` | Video planning and script drafting |
| `yt-package` | Titles and thumbnail text |
| `yt-shorts` | Short-form content discovery and packaging |

### Claude Code

1. Open the relevant skill directory.
2. Read its `SKILL.md` instructions.
3. Install or copy the skill using the supported skill-loading method for your Claude Code version.
4. Start a new task that matches the skill's purpose and verify that the agent loads the instructions.

### OpenAI Codex

1. Open the relevant skill directory.
2. Read its `SKILL.md` instructions.
3. Place or install the skill using the supported skill-loading method for your Codex version.
4. Start a matching task and verify that the agent loads the instructions.

Skill discovery and installation conventions can change between agent versions. Check the official documentation for your installed version before choosing a global or project-specific location.

## 📁 Project Structure

```text
youtube-creator-agent/
├── .github/
│   └── ISSUE_TEMPLATE/
├── docs/
├── examples/
│   └── sample_transcript.txt
├── skills/
│   ├── yt-script/
│   ├── yt-package/
│   └── yt-shorts/
├── tests/
│   └── test_creatorpilot.py
├── tools/
│   └── creatorpilot.py
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

## 🧪 Testing

Run the automated tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

Tests cover the included utility behavior, including timestamp conversion, text checks, and transcript clip candidate handling.

Please run the tests on your own machine after making changes. If a test fails, include the command and error output when opening an issue.

## 🗺️ Roadmap

- [x] Hook-scoring heuristic
- [x] Title and thumbnail text checks
- [x] Timestamped transcript clip suggestions
- [x] Reusable creator workflow skills
- [x] Sample transcript and unit tests
- [ ] More comprehensive script-quality checks
- [ ] Multilingual and Hinglish support
- [ ] Optional YouTube Analytics CSV analysis
- [ ] Continuous integration and release automation

Roadmap items are planned improvements, not existing features.

## 🤝 Contributing

Contributions are welcome! You can help by:

- Adding test cases and edge cases
- Improving the clarity of tool feedback
- Expanding examples and documentation
- Improving multilingual support
- Proposing useful creator workflows

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🔗 Project

**CreatorPilot AI — YouTube Creator Agent**

Repository: https://github.com/Rohit-Kumar-AI/youtube-creator-agent

Built as an independent open-source project for practical, reusable YouTube creator workflows. Inspired by the broader ecosystem of YouTube agent skills; not affiliated with or a copy of any similarly named project.

If you find it useful, consider starring the repository ⭐ and contributing improvements.
