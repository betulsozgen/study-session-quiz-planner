import os
from file_saver import save_session

SAMPLE_INPUTS = {
    "subject": "Biology",
    "topic": "Cell division",
    "days_until_test": 5,
    "difficulty": "medium",
    "num_questions": 3,
}


def test_save_session_creates_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    file_path = save_session(SAMPLE_INPUTS, "Study plan here.", "Quiz here.")
    assert os.path.exists(file_path)


def test_save_session_file_contains_study_plan(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    file_path = save_session(SAMPLE_INPUTS, "Study plan here.", "Quiz here.")
    content = open(file_path).read()
    assert "Study plan here." in content


def test_save_session_file_contains_quiz(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    file_path = save_session(SAMPLE_INPUTS, "Study plan here.", "Quiz here.")
    content = open(file_path).read()
    assert "Quiz here." in content


def test_save_session_filename_includes_subject(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    file_path = save_session(SAMPLE_INPUTS, "Study plan here.", "Quiz here.")
    assert "biology" in os.path.basename(file_path)
