import random


def generate_quiz(inputs: dict, bank: dict) -> str:
    subject = inputs["subject"]
    topic = inputs["topic"]
    difficulty = inputs["difficulty"]
    n = inputs["num_questions"]

    pool = bank.get(subject, {}).get(topic, {}).get(difficulty, [])
    selected = random.sample(pool, min(n, len(pool)))

    question_lines = []
    answer_lines = ["ANSWER KEY:"]

    for i, item in enumerate(selected, start=1):
        question_lines.append(f"{i}. {item['q']}")
        answer_lines.append(f"{i}. {item['a']}")

    return "\n".join(question_lines) + "\n\n" + "\n".join(answer_lines)
