# Study Session Quiz Planner

A Python CLI tool that uses the Claude AI to generate a personalized day-by-day study plan
and a short quiz, then saves the session to a text file.

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
```

## Run

```bash
python main.py
```

## Test

```bash
pytest
```

## What it does

1. Prompts you for: subject, topic, days until test, difficulty level, number of questions
2. Calls Claude to generate a day-by-day study plan
3. Calls Claude to generate a quiz with answers
4. Prints both to the terminal
5. Saves everything to `saved_sessions/`
