from evaluation.evaluator import evaluate

def optimize():
    results = evaluate()
    failures = [r for r in results if not r["structure_ok"]]

    if not failures:
        print("No failures detected")
    else:
        print("Failures:", failures)


if __name__ == "__main__":
    optimize()
