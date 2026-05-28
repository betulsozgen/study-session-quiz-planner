from question_bank import QUESTION_BANK
from study_planner import generate_study_plan
from quiz_generator import generate_quiz
from file_saver import save_session

VALID_DIFFICULTIES = ["easy", "medium", "hard"]


def _pick_from_menu(prompt: str, options: list) -> str:
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        raw = input(prompt).strip()
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return options[idx]
            print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a number.")


def get_user_input(bank: dict) -> dict:
    subjects = list(bank.keys())
    print("Available subjects:")
    subject = _pick_from_menu("Select a subject: ", subjects)

    topics = list(bank[subject].keys())
    print(f"\nAvailable topics in {subject}:")
    topic = _pick_from_menu("Select a topic: ", topics)

    days_until_test = None
    while days_until_test is None:
        raw = input("\nDays until test: ").strip()
        try:
            val = int(raw)
            if val <= 0:
                print("Days must be a positive number. Please try again.")
            else:
                days_until_test = val
        except ValueError:
            print("Please enter a whole number (e.g. 7).")

    difficulty = None
    while difficulty is None:
        raw = input("Difficulty (easy / medium / hard): ").strip().lower()
        if raw in VALID_DIFFICULTIES:
            difficulty = raw
        else:
            print(f"Please choose one of: {', '.join(VALID_DIFFICULTIES)}.")

    max_q = len(bank[subject][topic].get(difficulty, []))
    num_questions = None
    while num_questions is None:
        raw = input(f"Number of quiz questions (1–{max_q} available): ").strip()
        try:
            val = int(raw)
            if val <= 0:
                print("Must be at least 1.")
            elif val > max_q:
                print(f"Only {max_q} {difficulty} questions available. Please enter a smaller number.")
            else:
                num_questions = val
        except ValueError:
            print("Please enter a whole number.")

    return {
        "subject": subject,
        "topic": topic,
        "days_until_test": days_until_test,
        "difficulty": difficulty,
        "num_questions": num_questions,
    }


def main():
    print("=" * 52)
    print("       STUDY SESSION QUIZ PLANNER")
    print("=" * 52)
    print()

    inputs = get_user_input(QUESTION_BANK)

    print("\n" + "=" * 52)
    print("  STUDY PLAN")
    print("=" * 52)
    study_plan = generate_study_plan(inputs)
    print(study_plan)

    print("\n" + "=" * 52)
    print("  QUIZ")
    print("=" * 52)
    quiz = generate_quiz(inputs, QUESTION_BANK)
    print(quiz)

    file_path = save_session(inputs, study_plan, quiz)
    print("\n" + "=" * 52)
    print(f"  Session saved to: {file_path}")
    print("=" * 52)


if __name__ == "__main__":
    main()
