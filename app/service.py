from app.prompt import build_prompt
from app.validator import validate_output
from app.utils.model import ModelClient
from app.utils.json_utils import safe_parse, repair_json
from app.utils.input_utils import validate_input
from app.utils.logger import get_logger

logger = get_logger(__name__)
model = ModelClient()


def generate_structured_output(input_text: str, schema: dict):
    if not isinstance(schema, dict):
        return {"error": "Invalid schema format"}

    valid, processed_input, truncated = validate_input(input_text)

    if not valid:
        return {"error": processed_input}

    if truncated:
        logger.warning("Input was truncated due to length")

    prompt = build_prompt(processed_input, schema)

    logger.info("Calling model")

    raw = model.generate(prompt)

    parsed = safe_parse(raw)

    if not parsed:
        logger.warning("Parsing failed, attempting repair")
        parsed = repair_json(raw, schema)

    if not parsed:
        return {"error": "Failed to generate valid structured output"}

    return validate_output(parsed, schema)
