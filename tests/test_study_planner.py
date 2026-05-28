from study_planner import generate_study_plan

SAMPLE_INPUTS = {
    "subject": "Biology",
    "topic": "Cell Division",
    "days_until_test": 5,
    "difficulty": "medium",
    "num_questions": 3,
}


def test_generate_study_plan_returns_string():
    result = generate_study_plan(SAMPLE_INPUTS)
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_study_plan_contains_topic():
    result = generate_study_plan(SAMPLE_INPUTS)
    assert "Cell Division" in result


def test_generate_study_plan_contains_subject():
    result = generate_study_plan(SAMPLE_INPUTS)
    assert "Biology" in result


def test_generate_study_plan_has_correct_day_count():
    result = generate_study_plan(SAMPLE_INPUTS)
    assert "Day 5:" in result or "Day 5 (Review):" in result
    assert "Day 6:" not in result


def test_generate_study_plan_last_day_is_review():
    result = generate_study_plan(SAMPLE_INPUTS)
    assert "Review" in result


def test_generate_study_plan_difficulty_affects_output():
    easy = generate_study_plan({**SAMPLE_INPUTS, "difficulty": "easy"})
    hard = generate_study_plan({**SAMPLE_INPUTS, "difficulty": "hard"})
    assert easy != hard
