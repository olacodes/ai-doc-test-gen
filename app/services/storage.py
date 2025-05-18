import os

BASE_OUTPUT_DIR = "outputs"


def save_job_output(job_id: str, docs: str, tests: str):
    job_dir = os.path.join(BASE_OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)

    docs_path = os.path.join(job_dir, "docs.md")
    tests_path = os.path.join(job_dir, "tests.py")

    with open(docs_path, "w", encoding="utf-8") as f:
        f.write(docs)

    with open(tests_path, "w", encoding="utf-8") as f:
        f.write(tests)

    return docs_path, tests_path


def get_job_output(job_id: str) -> dict:
    job_dir = os.path.join(BASE_OUTPUT_DIR, job_id)
    docs_path = os.path.join(job_dir, "docs.md")
    tests_path = os.path.join(job_dir, "tests.py")

    if not os.path.exists(docs_path) or not os.path.exists(tests_path):
        raise FileNotFoundError("Result not ready yet or job not found.")

    with open(docs_path, "r", encoding="utf-8") as f:
        docs = f.read()

    with open(tests_path, "r", encoding="utf-8") as f:
        tests = f.read()

    return {"job_id": job_id, "documentation": docs, "unit_tests": tests}
