_EASY_TASKS = [
    "Read your notes on {topic} from start to finish.",
    "Highlight key terms in your {subject} notes on {topic}.",
    "Write out the definition of {topic} in your own words.",
    "Re-read the {topic} section in your textbook or class materials.",
    "List 5 key facts about {topic} from memory.",
    "Look at any diagrams or visuals related to {topic}.",
]

_MEDIUM_TASKS = [
    "Review your notes and highlight the most important concepts in {topic}.",
    "Complete practice problems related to {topic}.",
    "Explain {topic} in your own words without looking at your notes.",
    "Create a concept map connecting the key ideas within {topic}.",
    "Find two real-world examples of {topic} in {subject}.",
    "Answer 5 self-quiz questions on {topic}.",
    "Compare two key components or aspects of {topic}.",
    "Identify anything about {topic} that still feels unclear and look it up.",
]

_HARD_TASKS = [
    "Deep-read all materials on {topic} and annotate with your own comments.",
    "Complete a timed practice test on {topic} — 20 minutes, no notes.",
    "Teach {topic} back to yourself from a blank page, then check your notes.",
    "Identify connections between {topic} and three other concepts in {subject}.",
    "Write a detailed summary of {topic} from memory, then verify its accuracy.",
    "Work through the most difficult practice problems on {topic}.",
    "Critically analyze edge cases and exceptions related to {topic}.",
    "Create 5 hard questions about {topic}, answer them, then check your answers.",
]

_REVIEW_TASKS = [
    "Lightly skim your summary notes on {topic}.",
    "Review key definitions only — no new material today.",
    "Do a quick mental walkthrough of the core ideas in {topic}.",
    "Check any concepts in {topic} that still feel uncertain.",
    "Rest, eat well, and stay confident — you are prepared!",
]

_TASKS_PER_DAY = {"easy": 2, "medium": 3, "hard": 4}
_REVIEW_COUNT = {"easy": 3, "medium": 3, "hard": 4}


def _fmt(template: str, inputs: dict) -> str:
    return template.format(topic=inputs["topic"], subject=inputs["subject"])


def generate_study_plan(inputs: dict) -> str:
    days = inputs["days_until_test"]
    difficulty = inputs["difficulty"]
    task_pool = {"easy": _EASY_TASKS, "medium": _MEDIUM_TASKS, "hard": _HARD_TASKS}.get(
        difficulty, _MEDIUM_TASKS
    )
    tasks_per_day = _TASKS_PER_DAY.get(difficulty, 3)
    review_count = _REVIEW_COUNT.get(difficulty, 3)

    lines = []
    pool_idx = 0

    for day in range(1, days + 1):
        is_last = day == days
        label = f"Day {day}:" if not is_last else f"Day {day} (Review):"
        lines.append(label)

        if is_last:
            for task in _REVIEW_TASKS[:review_count]:
                lines.append(f"  - {_fmt(task, inputs)}")
        else:
            for _ in range(tasks_per_day):
                lines.append(f"  - {_fmt(task_pool[pool_idx % len(task_pool)], inputs)}")
                pool_idx += 1

        lines.append("")

    return "\n".join(lines).strip()
