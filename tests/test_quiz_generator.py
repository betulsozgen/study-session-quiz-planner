from unittest.mock import MagicMock
from quiz_generator import build_quiz_prompt, generate_quiz

SAMPLE_INPUTS = {
    "subject": "Biology",
    "topic": "Cell division",
    "days_until_test": 5,
    "difficulty": "medium",
    "num_questions": 3,
}


def test_build_quiz_prompt_contains_difficulty():
    prompt = build_quiz_prompt(SAMPLE_INPUTS)
    assert "medium" in prompt


def test_build_quiz_prompt_contains_num_questions():
    prompt = build_quiz_prompt(SAMPLE_INPUTS)
    assert "3" in prompt


def test_build_quiz_prompt_contains_topic():
    prompt = build_quiz_prompt(SAMPLE_INPUTS)
    assert "Cell division" in prompt


def test_build_quiz_prompt_contains_subject():
    prompt = build_quiz_prompt(SAMPLE_INPUTS)
    assert "Biology" in prompt


def test_generate_quiz_returns_text():
    mock_client = MagicMock()
    mock_client.messages.create.return_value.content[0].text = "1. What is mitosis?"
    result = generate_quiz(mock_client, SAMPLE_INPUTS)
    assert result == "1. What is mitosis?"
    mock_client.messages.create.assert_called_once()
