import json
import os
from app.service import generate_structured_output

BASE = os.path.dirname(__file__)
TEST_FILE = os.path.join(BASE, "test_cases.json")


def evaluate():
    with open(TEST_FILE) as f:
        test_cases = json.load(f)

    results = []

    for case in test_cases:
        output = generate_structured_output(case["input"], case["schema"])

        structure_ok = all(k in output for k in case["schema"])

        results.append({
            "input": case["input"],
            "structure_ok": structure_ok
        })

        print("\nInput:", case["input"])
        print("Output:", output)

    return results


if __name__ == "__main__":
    res = evaluate()
    print("\nSummary:", res)
