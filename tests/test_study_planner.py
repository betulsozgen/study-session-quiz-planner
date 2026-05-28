from unittest.mock import MagicMock, patch
from study_planner import build_study_plan_prompt, generate_study_plan

SAMPLE_INPUTS = {
    "subject": "Biology",
    "topic": "Cell division",
    "days_until_test": 5,
    "difficulty": "medium",
    "num_questions": 3,
}


def test_build_study_plan_prompt_contains_subject():
    prompt = build_study_plan_prompt(SAMPLE_INPUTS)
    assert "Biology" in prompt


def test_build_study_plan_prompt_contains_topic():
    prompt = build_study_plan_prompt(SAMPLE_INPUTS)
    assert "Cell division" in prompt


def test_build_study_plan_prompt_contains_days():
    prompt = build_study_plan_prompt(SAMPLE_INPUTS)
    assert "5" in prompt


def test_build_study_plan_prompt_contains_difficulty():
    prompt = build_study_plan_prompt(SAMPLE_INPUTS)
    assert "medium" in prompt


def test_generate_study_plan_returns_text():
    mock_client = MagicMock()
    mock_client.messages.create.return_value.content[0].text = "Day 1: Read chapter 1."
    result = generate_study_plan(mock_client, SAMPLE_INPUTS)
    assert result == "Day 1: Read chapter 1."
    mock_client.messages.create.assert_called_once()
