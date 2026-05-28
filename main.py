import os
import anthropic

from study_planner import generate_study_plan
from quiz_generator import generate_quiz
from file_saver import save_session

VALID_DIFFICULTIES = ["easy", "medium", "hard"]


def get_user_input() -> dict:
    """Prompt the user for all session inputs and return them as a dict."""
    # TODO (Task 2): implement validation for each field
    subject = input("Subject (e.g. Biology): ").strip()
    topic = input("Topic (e.g. Cell division): ").strip()

    days_until_test = input("Days until test: ").strip()
    # TODO: validate days_until_test is a positive integer

    difficulty = input("Difficulty (easy / medium / hard): ").strip().lower()
    # TODO: validate difficulty is one of VALID_DIFFICULTIES

    num_questions = input("Number of quiz questions: ").strip()
    # TODO: validate num_questions is a positive integer

    return {
        "subject": subject,
        "topic": topic,
        "days_until_test": int(days_until_test),
        "difficulty": difficulty,
        "num_questions": int(num_questions),
    }


def main():
    """Orchestrate user input, study plan, quiz, and file saving."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.")
        return

    client = anthropic.Anthropic(api_key=api_key)
    inputs = get_user_input()

    # TODO (Task 3): generate and print study plan
    print("\nGenerating your study plan...\n")
    study_plan = generate_study_plan(client, inputs)
    print(study_plan)

    # TODO (Task 4): generate and print quiz
    print("\nGenerating your quiz...\n")
    quiz = generate_quiz(client, inputs)
    print(quiz)

    # TODO (Task 5): save session to file
    file_path = save_session(inputs, study_plan, quiz)
    print(f"\nSession saved to: {file_path}")


if __name__ == "__main__":
    main()
