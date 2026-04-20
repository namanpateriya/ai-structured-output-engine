import json
import os
from statistics import mean
from app.service import generate_structured_output

BASE = os.path.dirname(__file__)
TEST_FILE = os.path.join(BASE, "test_cases.json")


def check_structure(output, schema):
    return all(k in output for k in schema)


def check_types(output, schema):
    for k, v in schema.items():
        if isinstance(v, list) and not isinstance(output.get(k), list):
            return False
        if isinstance(v, str) and not isinstance(output.get(k), str):
            return False
    return True


def evaluate():
    with open(TEST_FILE) as f:
        cases = json.load(f)

    results = []

    for case in cases:
        output = generate_structured_output(case["input"], case["schema"])

        if "error" in output:
            results.append({"error": True})
            continue

        structure_ok = check_structure(output, case["schema"])
        type_ok = check_types(output, case["schema"])

        results.append({
            "structure_ok": structure_ok,
            "type_ok": type_ok
        })

        print("\nInput:", case["input"])
        print("Output:", output)

    return results


def summarize(results):
    valid = [r for r in results if "error" not in r]

    summary = {
        "structure_accuracy": mean([r["structure_ok"] for r in valid]) if valid else 0,
        "type_accuracy": mean([r["type_ok"] for r in valid]) if valid else 0
    }

    print("\n=== SUMMARY ===")
    for k, v in summary.items():
        print(f"{k}: {round(v,2)}")


if __name__ == "__main__":
    res = evaluate()
    summarize(res)
