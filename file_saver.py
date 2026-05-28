import os
from datetime import datetime


def save_session(inputs: dict, study_plan: str, quiz: str) -> str:
    """Save the study plan and quiz to a .txt file in saved_sessions/. Returns the file path."""
    os.makedirs("saved_sessions", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    subject_slug = inputs["subject"].replace(" ", "_").lower()
    filename = f"{subject_slug}_{timestamp}.txt"
    file_path = os.path.join("saved_sessions", filename)

    # TODO (Task 5): format and write the file content
    content = (
        f"STUDY SESSION\n"
        f"=============\n"
        f"Subject:    {inputs['subject']}\n"
        f"Topic:      {inputs['topic']}\n"
        f"Days until test: {inputs['days_until_test']}\n"
        f"Difficulty: {inputs['difficulty']}\n"
        f"Questions:  {inputs['num_questions']}\n\n"
        f"STUDY PLAN\n"
        f"----------\n"
        f"{study_plan}\n\n"
        f"QUIZ\n"
        f"----\n"
        f"{quiz}\n"
    )

    with open(file_path, "w") as f:
        f.write(content)

    return file_path
