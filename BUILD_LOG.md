# Build Log

Track progress task by task as the project is built out.

---

## Task 1 — Scaffold repo ✅
- Created project file structure
- Added placeholder source files and test files
- Added CLAUDE.md, README.md, .gitignore, requirements.txt

## Task 2 — User input collection (in progress)
- [ ] `get_user_input()` in `main.py`
- [ ] Validates: difficulty must be easy/medium/hard, days and questions must be positive integers

## Task 3 — Study plan generation
- [ ] `build_study_plan_prompt()` in `study_planner.py`
- [ ] `generate_study_plan()` in `study_planner.py`

## Task 4 — Quiz generation
- [ ] `build_quiz_prompt()` in `quiz_generator.py`
- [ ] `generate_quiz()` in `quiz_generator.py`

## Task 5 — File saving
- [ ] `save_session()` in `file_saver.py`
- [ ] Creates `saved_sessions/` if needed
- [ ] Filename format: `{subject}_{YYYY-MM-DD}_{HH-MM}.txt`

## Task 6 — Wire it all together
- [ ] `main()` calls all modules in sequence
- [ ] Prints study plan and quiz to terminal
- [ ] Confirms save location to user

## Task 7 — Tests passing
- [ ] All tests in `tests/test_study_planner.py` pass
- [ ] All tests in `tests/test_quiz_generator.py` pass
- [ ] `pytest` runs clean with no live API calls
