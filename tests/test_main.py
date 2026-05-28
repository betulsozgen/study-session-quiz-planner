from unittest.mock import patch
from main import get_user_input

MOCK_BANK = {
    "Biology": {
        "Cell Division": {
            "easy": [
                {"q": "What is mitosis?", "a": "Cell division producing two identical cells."},
                {"q": "What are the phases?", "a": "Prophase, metaphase, anaphase, telophase."},
                {"q": "What is cytokinesis?", "a": "Division of the cytoplasm."},
            ],
            "medium": [
                {"q": "Compare mitosis and meiosis.", "a": "Mitosis: 2 diploid; Meiosis: 4 haploid."},
            ],
            "hard": [
                {"q": "How do mutations cause cancer?", "a": "Disable checkpoints."},
            ],
        }
    },
    "Math": {
        "Algebra": {
            "easy": [
                {"q": "What is a variable?", "a": "A symbol for an unknown value."},
            ],
            "medium": [],
            "hard": [],
        }
    },
}


def test_get_user_input_returns_correct_dict():
    # "1" → Biology, "1" → Cell Division, "5" days, "easy", "2" questions
    with patch("builtins.input", side_effect=["1", "1", "5", "easy", "2"]):
        result = get_user_input(MOCK_BANK)
    assert result == {
        "subject": "Biology",
        "topic": "Cell Division",
        "days_until_test": 5,
        "difficulty": "easy",
        "num_questions": 2,
    }


def test_get_user_input_rejects_invalid_subject_number():
    # "9" is out of range, "1" retries successfully
    with patch("builtins.input", side_effect=["9", "1", "1", "7", "easy", "1"]):
        result = get_user_input(MOCK_BANK)
    assert result["subject"] == "Biology"


def test_get_user_input_rejects_invalid_difficulty():
    # "extreme" is invalid; "easy" succeeds on retry
    with patch("builtins.input", side_effect=["1", "1", "5", "extreme", "easy", "1"]):
        result = get_user_input(MOCK_BANK)
    assert result["difficulty"] == "easy"


def test_get_user_input_rejects_non_integer_days():
    # "abc" is invalid; "5" succeeds on retry
    with patch("builtins.input", side_effect=["1", "1", "abc", "5", "easy", "1"]):
        result = get_user_input(MOCK_BANK)
    assert result["days_until_test"] == 5


def test_get_user_input_rejects_too_many_questions():
    # Bank has 3 easy questions; asking for 10 is rejected, 2 succeeds
    with patch("builtins.input", side_effect=["1", "1", "5", "easy", "10", "2"]):
        result = get_user_input(MOCK_BANK)
    assert result["num_questions"] == 2
