# CLAUDE.md

## What this project is

A Python CLI app that presents a menu of subjects and topics, generates a
personalized day-by-day study plan, pulls random quiz questions from a local
question bank, and saves the full session to a text file in `saved_sessions/`.

No external APIs or API keys required — runs entirely with the Python standard
library plus `pytest`.

## Stack

- Python 3.10+
- `pytest` for testing
- Standard library only (`random`, `os`, `datetime`)

## How to run

```bash
python main.py
```

No environment variables needed.

## How to run tests

```bash
pytest
```

All tests run without network access or API keys.

## File responsibilities

| File | Responsibility |
|------|---------------|
| `main.py` | CLI entry point, numbered menus for subject/topic, input validation, orchestration |
| `question_bank.py` | All quiz questions organized by subject → topic → difficulty |
| `study_planner.py` | Rule-based day-by-day study plan generator |
| `quiz_generator.py` | Randomly samples questions from the bank by difficulty |
| `file_saver.py` | Saves session output to `saved_sessions/{subject}_{date}_{time}.txt` |

## Question bank structure

```python
QUESTION_BANK = {
    "Subject": {
        "Topic": {
            "easy":   [{"q": "...", "a": "..."}, ...],
            "medium": [...],
            "hard":   [...],
        }
    }
}
```

Current subjects: Biology, Math, History, Computer Science

## Conventions

- Do not edit `tests/` to make them pass — fix source files instead.
- Keep changes scoped to the task at hand.
- Read the test file first — it describes the expected behavior exactly.
- `saved_sessions/` is auto-created at runtime and is git-ignored.
- To add a new subject or topic, edit `question_bank.py` only — no other files need to change.
