# Build Log

---

## Task 1 — Scaffold repo ✅
- Created project file structure
- Added CLAUDE.md, README.md, .gitignore, requirements.txt
- Placeholder source files and test files committed

## Task 2 — User input collection ✅
- `get_user_input(bank)` in `main.py`
- Numbered menus for subject and topic selection from the question bank
- Validates: difficulty must be easy/medium/hard, days and questions must be
  positive integers, num_questions capped at bank size for chosen difficulty

## Task 3 — Study plan generation ✅
- `generate_study_plan(inputs)` in `study_planner.py`
- Rule-based: rotating task pools per difficulty (easy/medium/hard)
- 2–4 tasks per day depending on difficulty; final day always shows review tasks

## Task 4 — Quiz generation ✅
- `generate_quiz(inputs, bank)` in `quiz_generator.py`
- Randomly samples N questions from `QUESTION_BANK[subject][topic][difficulty]`
- Output includes numbered questions followed by a labeled ANSWER KEY section

## Task 5 — Question bank ✅
- `question_bank.py` with 135 real questions
- 4 subjects: Biology, Math, History, Computer Science
- 9 topics total; 5–6 questions per difficulty level per topic

## Task 6 — File saving ✅
- `save_session(inputs, study_plan, quiz)` in `file_saver.py`
- Auto-creates `saved_sessions/` if missing
- Filename format: `{subject}_{YYYY-MM-DD}_{HH-MM}.txt`
- File contains session metadata header, full study plan, and full quiz

## Task 7 — Wire it all together ✅
- `main()` orchestrates menus → study plan → quiz → file save
- Prints study plan and quiz to terminal with clear section headers
- Confirms save path to user after writing

## Task 8 — Tests ✅
- 21 tests across 4 test files, all passing
- No live API calls, no environment variables required
- `pytest` runs clean in under 1 second
