# YouTube Creator Agent 🚀

**Open-source AI agent skills and Python tools for YouTube creators.**

YouTube Creator Agent helps creators improve video hooks, evaluate titles, discover potential Shorts moments from transcripts, and streamline content planning using reusable AI agent skills.

Built as an independent project for creators experimenting with **Claude Code, Codex, and Python**.

[![GitHub stars](https://img.shields.io/github/stars/Rohit-Kumar-AI/youtube-creator-agent?style=for-the-badge)](https://github.com/Rohit-Kumar-AI/youtube-creator-agent/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Rohit-Kumar-AI/youtube-creator-agent?style=for-the-badge)](https://github.com/Rohit-Kumar-AI/youtube-creator-agent/issues)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

## 📑 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [Agent Skills](#-agent-skills)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

| Feature | Description |
|---|---|
| 🎣 Hook Checker | Analyze a video opening with a lightweight heuristic score and improvement feedback. |
| 🏷️ Title Checker | Review title and thumbnail text for basic quality issues and readability. |
| ✂️ Shorts Moment Finder | Suggest potential short-form clips from a timestamped transcript. |
| 📝 Script Skill | Reusable instructions for planning and drafting YouTube scripts. |
| 📦 Video Packaging Skill | Reusable instructions for developing titles, descriptions, and thumbnail concepts. |
| 📱 Shorts Skill | Reusable instructions for finding and shaping short-form content. |

**Design goals**
- Simple local Python tools.
- No API key required for the included utility scripts.
- Reusable skill instructions for AI coding assistants.
- Beginner-friendly structure that contributors can extend.
- No mandatory external Python dependencies for the core utilities.

> **Note:** Scores and suggestions from the Python utilities are heuristic, not guarantees of video performance. AI agent skills provide instructions; their results depend on the AI assistant and context used.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Rohit-Kumar-AI/youtube-creator-agent.git
cd youtube-creator-agent
```

### 2. Check Python

Python 3.10 or later is recommended.

```bash
python --version
```

### 3. Explore the available commands

```bash
python tools/creatorpilot.py --help
```

### 4. Run the tests

```bash
python -m unittest discover -s tests -v
```

The core utilities are designed to run locally without API credentials.

## 💡 Usage Examples

### 1. Check a video hook

```bash
python tools/creatorpilot.py hook "I wasted 30 days learning Python the wrong way."
```

Use the feedback as a starting point for making the opening clearer, more specific, and more engaging.

### 2. Check a title and thumbnail text

```bash
python tools/creatorpilot.py title "I learned Python in 30 days" --thumbnail "30 days"
```

Use the output to identify basic title or thumbnail-text issues before publishing.

### 3. Find potential Shorts moments

```bash
python tools/creatorpilot.py clips examples/sample_transcript.txt
```

The transcript should use the format expected by the utility, including timestamps where required. The tool suggests potential moments; review the original video before selecting a clip.

**Tip:** Run `python tools/creatorpilot.py --help` if your local version uses different command options.

## 🤖 Agent Skills

The repository includes reusable skill instructions that can guide an AI assistant through common YouTube workflows.

### `yt-script`

Use for:
- Brainstorming video ideas.
- Structuring a script around a clear audience.
- Improving hooks and transitions.
- Organizing a video into logical sections.
- Drafting calls to action.

### `yt-package`

Use for:
- Brainstorming video titles.
- Developing thumbnail concepts.
- Aligning the title, thumbnail, and video promise.
- Drafting video descriptions.
- Reviewing packaging ideas for clarity.

### `yt-shorts`

Use for:
- Reviewing transcripts for compelling moments.
- Identifying potential short-form clips.
- Developing opening hooks.
- Suggesting concise clip structures.
- Repurposing long-form ideas into short-form concepts.

### Using the skills

1. Open the relevant skill directory in this repository.
2. Read its instructions.
3. Follow the integration instructions supported by your AI coding assistant.
4. Provide your video topic, target audience, transcript, or other relevant context.
5. Review and refine the generated output before publishing.

Skill discovery and installation conventions may differ between AI assistants and versions. Consult the documentation for your chosen assistant rather than assuming every skill directory is automatically installed.

## 📂 Project Structure

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
│   └── sample_transcript.txt
├── docs/
├── .github/
│   └── ISSUE_TEMPLATE/
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

The exact contents may evolve as the project develops.

## 🧪 Testing

Run the test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

When contributing, add tests for new utility behavior and verify that existing tests continue to pass.

## 🗺️ Roadmap

### Core utilities
- [x] Hook scoring utility
- [x] Basic title and thumbnail-text checks
- [x] Timestamped transcript clip suggestions
- [x] Local unit tests

### Future improvements
- [ ] More advanced hook and title analysis
- [ ] Configurable scoring rules
- [ ] Additional transcript formats
- [ ] Improved Shorts selection and ranking
- [ ] More creator workflows and reusable skills
- [ ] Expanded examples and documentation

Roadmap items are plans, not promises or claims that the features already exist.

## 🤝 Contributing

Contributions, suggestions, bug reports, and feature requests are welcome!

1. Check the existing issues before opening a new one.
2. Describe the problem or improvement clearly.
3. Keep changes focused and easy to review.
4. Add or update tests when appropriate.
5. Submit a pull request with a concise explanation of the change.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before contributing, and use the [Issues page](https://github.com/Rohit-Kumar-AI/youtube-creator-agent/issues) to report bugs or suggest improvements.

## 📄 License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.

## 👨‍💻 Author

**Rohit Kumar**

- GitHub: [@Rohit-Kumar-AI](https://github.com/Rohit-Kumar-AI)
- Project repository: [youtube-creator-agent](https://github.com/Rohit-Kumar-AI/youtube-creator-agent)

If you find this project useful, consider giving it a ⭐ on GitHub and sharing suggestions through Issues.

---

*YouTube Creator Agent is an independent open-source project and is not affiliated with or endorsed by YouTube, Anthropic, OpenAI, or other AI providers.*
