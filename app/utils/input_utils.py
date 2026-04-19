import os

MAX_INPUT_LENGTH = int(os.getenv("MAX_INPUT_LENGTH", "2000"))


def validate_input(input_text: str):
    if not input_text or not input_text.strip():
        return False, "Empty input"

    if len(input_text) > MAX_INPUT_LENGTH:
        input_text = input_text[:MAX_INPUT_LENGTH]

    return True, input_text
