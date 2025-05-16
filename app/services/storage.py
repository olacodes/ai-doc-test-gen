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
