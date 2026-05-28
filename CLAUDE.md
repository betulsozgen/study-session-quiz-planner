# CLAUDE.md

## What this project is

A Python CLI app that uses the Claude API to generate a personalized study plan and quiz,
then saves the session to a text file in `saved_sessions/`.

## Stack

- Python 3.10+
- `anthropic` SDK (Claude API)
- `pytest` for testing
- Standard library only (no Flask, no database)

## How to run

```bash
python main.py
```

Requires `ANTHROPIC_API_KEY` set as an environment variable.

## How to run tests

```bash
pytest
```

Tests mock the Claude client — no live API key needed.

## File responsibilities

| File | Responsibility |
|------|---------------|
| `main.py` | CLI entry point, user input collection, orchestration |
| `study_planner.py` | Build study plan prompt, call Claude for study plan |
| `quiz_generator.py` | Build quiz prompt, call Claude for quiz questions |
| `file_saver.py` | Save session output to `saved_sessions/` as a `.txt` file |

## Conventions

- Do not edit `tests/` to make them pass — fix source files instead.
- Keep changes scoped to the task at hand.
- Read the test file first — it describes the expected behavior exactly.
- Always read a task description before writing code for it.
- `saved_sessions/` is auto-created at runtime and is git-ignored.
