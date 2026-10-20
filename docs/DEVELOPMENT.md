# Development notes

## Design goals
- Standard-library-only core.
- Explainable heuristics; no claims of guaranteed performance.
- Human approval before publishing.
- Shared Agent Skills content for Claude Code and Codex.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Timestamp input
The transcript utility expects one timestamped segment per line, for example:
`00:01:23.400 This is the spoken text.`

Supported timestamp forms include `MM:SS`, `HH:MM:SS`, and optional decimal fractions. Candidate ranking is intentionally simple and should be validated by a person.
