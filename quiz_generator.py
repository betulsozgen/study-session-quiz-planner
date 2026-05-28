def build_quiz_prompt(inputs: dict) -> str:
    """Return a Claude prompt string for generating a quiz with answers."""
    # TODO (Task 4): build a clear, detailed prompt
    return (
        f"Create a {inputs['difficulty']} difficulty quiz with exactly {inputs['num_questions']} "
        f"questions about {inputs['topic']} in {inputs['subject']}. "
        f"Number each question. After all questions, provide an answer key labeled 'Answer Key:' "
        f"with the correct answer for each question."
    )


def generate_quiz(client, inputs: dict) -> str:
    """Call the Claude API and return the quiz (questions + answer key) as a string."""
    # TODO (Task 4): call client.messages.create with the prompt
    prompt = build_quiz_prompt(inputs)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text
