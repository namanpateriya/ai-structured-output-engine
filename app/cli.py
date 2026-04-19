import argparse
import json
import sys
from app.service import generate_structured_output
from app.utils.logger import get_logger

logger = get_logger(__name__)

parser = argparse.ArgumentParser(description="AI Structured Output Engine")

parser.add_argument("--input", required=True)
parser.add_argument("--schema", required=True)

args = parser.parse_args()

try:
    schema = json.loads(args.schema)
except Exception:
    print("Invalid schema JSON")
    sys.exit(1)

result = generate_structured_output(args.input, schema)

print(json.dumps(result, indent=2))
