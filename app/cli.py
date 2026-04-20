import argparse
import json
import sys
from app.service import generate_structured_output

parser = argparse.ArgumentParser(description="AI Structured Output Engine")

parser.add_argument("--input", required=True)
parser.add_argument("--schema", required=True)

args = parser.parse_args()

try:
    schema = json.loads(args.schema)
    if not isinstance(schema, dict):
        raise ValueError
except Exception:
    print("Invalid schema JSON")
    sys.exit(1)

result = generate_structured_output(args.input, schema)

print(json.dumps(result, indent=2))
