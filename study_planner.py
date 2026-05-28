def build_study_plan_prompt(inputs: dict) -> str:
    """Return a Claude prompt string for generating a day-by-day study plan."""
    # TODO (Task 3): build a clear, detailed prompt
    return (
        f"Create a day-by-day study plan for a student studying {inputs['subject']}, "
        f"specifically the topic: {inputs['topic']}. "
        f"They have {inputs['days_until_test']} days until their test and want a "
        f"{inputs['difficulty']} difficulty plan. "
        f"Format it as Day 1, Day 2, etc. with specific tasks for each day."
    )


def generate_study_plan(client, inputs: dict) -> str:
    """Call the Claude API and return the study plan as a string."""
    # TODO (Task 3): call client.messages.create with the prompt
    prompt = build_study_plan_prompt(inputs)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text
