def build_prompt(input_text: str, schema: dict):
    keys = ", ".join(schema.keys())

    return f"""
You are an AI system that converts unstructured text into structured JSON.

INPUT:
{input_text}

REQUIRED JSON KEYS:
{keys}

SCHEMA:
{schema}

RULES:
- Return STRICT JSON only
- Include ALL keys
- Do not add extra text
- Ensure valid JSON
"""
