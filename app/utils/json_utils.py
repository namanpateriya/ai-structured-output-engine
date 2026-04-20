import json
from app.utils.logger import get_logger
from app.utils.model import ModelClient

logger = get_logger(__name__)


def safe_parse(raw):
    if isinstance(raw, dict):
        return raw

    if not isinstance(raw, str):
        raw = str(raw)

    try:
        return json.loads(raw)
    except Exception:
        return None


def clean_json_text(text: str):
    text = text.strip()

    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("{") and part.endswith("}"):
                return part

    return text


def repair_json(raw_output: str, schema: dict):
    model = ModelClient()
    keys = ", ".join(schema.keys())

    prompt = f"""
Fix the following into VALID JSON.

REQUIRED KEYS:
{keys}

SCHEMA:
{schema}

Return ONLY JSON.

INPUT:
{raw_output}
"""

    try:
        fixed = model.generate(prompt)
        fixed = clean_json_text(fixed)
        return json.loads(fixed)

    except Exception as e:
        logger.error(f"JSON repair failed: {e}")
        return None
