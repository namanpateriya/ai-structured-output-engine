import json
from app.utils.logger import get_logger
from app.utils.model import ModelClient

logger = get_logger(__name__)
model = ModelClient()


def safe_parse(raw):
    if isinstance(raw, dict):
        return raw

    try:
        return json.loads(raw)
    except Exception:
        return None


def repair_json(raw_output: str, schema: dict):
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
        return json.loads(fixed)
    except Exception as e:
        logger.error(f"JSON repair failed: {e}")
        return None
