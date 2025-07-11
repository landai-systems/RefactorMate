from pathlib import Path
from typing import List
import difflib


def find_files(directory: Path, extensions: List[str]) -> List[Path]:
    """
    Recursively find files in a directory with given extensions.

    Args:
        directory (Path): Directory to search.
        extensions (List[str]): List of file extensions (e.g., ['py', 'js']).

    Returns:
        List[Path]: List of matching file paths.
    """
    return [f for f in directory.rglob("*") if f.suffix[1:].lower() in extensions and f.is_file()]


def read_file(file_path: Path) -> str:
    """
    Read the content of a file.

    Args:
        file_path (Path): Path to the file.

    Returns:
        str: File content.
    """
    return file_path.read_text(encoding="utf-8")


def write_diff(file_path: Path, original: str, diff: str) -> None:
    """
    Apply a diff patch to original content and overwrite the file.

    Args:
        file_path (Path): Path to the file.
        original (str): Original file content.
        diff (str): Diff string to apply.
    """
    patched_lines = list(difflib.restore(diff.splitlines(), 2))
    file_path.write_text("\n".join(patched_lines), encoding="utf-8")
