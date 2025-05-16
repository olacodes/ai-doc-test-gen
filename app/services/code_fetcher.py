import os
import shutil
import tempfile
from git import Repo


def clone_repo(repo_url: str) -> str:
    """Clone the repo and return path to local directory"""
    tmp_dir = tempfile.mkdtemp()
    Repo.clone_from(repo_url, tmp_dir)
    return tmp_dir


def collect_code_files(root_path: str, extensions=(".py", ".kt")) -> list[str]:
    """Find all code files with given extensions"""
    code_files = []
    for dirpath, _, filenames in os.walk(root_path):
        for file in filenames:
            if file.endswith(extensions):
                code_files.append(os.path.join(dirpath, file))
    return code_files


def read_code_snippets(file_paths: list[str]) -> list[str]:
    """Read each file’s content"""
    return [open(path, encoding="utf-8").read() for path in file_paths]
