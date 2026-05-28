from quiz_generator import generate_quiz

MOCK_BANK = {
    "Biology": {
        "Cell Division": {
            "easy": [
                {"q": "What is mitosis?", "a": "Cell division producing two identical cells."},
                {"q": "What are the phases of mitosis?", "a": "Prophase, metaphase, anaphase, telophase."},
                {"q": "What is cytokinesis?", "a": "Division of the cytoplasm into two cells."},
            ],
            "medium": [
                {"q": "Compare mitosis and meiosis.", "a": "Mitosis: 2 diploid cells; Meiosis: 4 haploid cells."},
                {"q": "What is the G1 checkpoint?", "a": "Ensures cell is ready to divide before DNA replication."},
            ],
            "hard": [
                {"q": "How do mutations cause cancer?", "a": "They disable checkpoints, allowing uncontrolled division."},
                {"q": "What is aneuploidy?", "a": "Having an abnormal number of chromosomes from spindle errors."},
            ],
        }
    }
}

SAMPLE_INPUTS = {
    "subject": "Biology",
    "topic": "Cell Division",
    "days_until_test": 5,
    "difficulty": "easy",
    "num_questions": 2,
}


def test_generate_quiz_returns_string():
    result = generate_quiz(SAMPLE_INPUTS, MOCK_BANK)
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_quiz_has_answer_key():
    result = generate_quiz(SAMPLE_INPUTS, MOCK_BANK)
    assert "ANSWER KEY:" in result


def test_generate_quiz_has_correct_question_count():
    result = generate_quiz(SAMPLE_INPUTS, MOCK_BANK)
    assert "1." in result
    assert "2." in result
    assert "3." not in result.split("ANSWER KEY:")[0]


def test_generate_quiz_questions_come_from_bank():
    result = generate_quiz(SAMPLE_INPUTS, MOCK_BANK)
    bank_questions = [item["q"] for item in MOCK_BANK["Biology"]["Cell Division"]["easy"]]
    questions_section = result.split("ANSWER KEY:")[0]
    matched = sum(1 for q in bank_questions if q in questions_section)
    assert matched == SAMPLE_INPUTS["num_questions"]


def test_generate_quiz_uses_correct_difficulty():
    hard_inputs = {**SAMPLE_INPUTS, "difficulty": "hard", "num_questions": 1}
    result = generate_quiz(hard_inputs, MOCK_BANK)
    hard_questions = [item["q"] for item in MOCK_BANK["Biology"]["Cell Division"]["hard"]]
    questions_section = result.split("ANSWER KEY:")[0]
    assert any(q in questions_section for q in hard_questions)


def test_generate_quiz_answers_match_questions():
    inputs = {**SAMPLE_INPUTS, "num_questions": 1}
    result = generate_quiz(inputs, MOCK_BANK)
    question_part, answer_part = result.split("ANSWER KEY:")
    assert "1." in question_part
    assert "1." in answer_part
