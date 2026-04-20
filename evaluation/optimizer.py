import json
from evaluation.evaluator import evaluate

def optimize():
    results = evaluate()

    failures = [r for r in results if not r.get("structure_ok")]

    print("\nFailures detected:", len(failures))

    if not failures:
        print("System stable")
        return

    print("\nSample failure:")
    print(json.dumps(failures[0], indent=2))


if __name__ == "__main__":
    optimize()
