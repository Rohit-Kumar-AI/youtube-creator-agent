# Contributing to YouTube Creator Agent — CreatorPilot AI

Thanks for helping make creator workflows more useful and transparent.

## Setup
- Python 3.10+
- No third-party packages required

Run `python -m unittest discover -s tests -v` before opening a pull request.

## Contribution guidelines
- Add tests for bug fixes and new heuristics.
- Keep scores explainable; document any scoring changes.
- Avoid claims that a heuristic guarantees views, retention, or virality.
- Keep the core tools dependency-free unless a strong reason is documented.
- Do not add telemetry, secrets, or automatic publishing.
- Keep skill instructions portable across Claude Code and Codex. If behavior differs, document the difference.

## Good first issues
- Add Hinglish-friendly test cases.
- Improve timestamp parsing for common transcript formats.
- Add accessible sample output to the README.
- Add CSV analytics import with clear input-column documentation.
