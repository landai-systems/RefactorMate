import argparse
import os
import sys
import json
from typing import List, Optional
from pathlib import Path
from utils.file_utils import find_files, read_file, write_diff
from utils.cli_utils import prompt_user
from utils.openai_utils import get_code_diff_suggestion


def process_file(file_path: Path, model: str) -> None:
    """
    Process a single file: send content to OpenAI, get diff, prompt user, apply diff.

    Args:
        file_path (Path): Path to the code file to process.
        model (str): OpenAI model name to use.
    """
    code = read_file(file_path)
    print(f"\n\033[1mAnalyzing {file_path}...\033[0m")

    diff = get_code_diff_suggestion(file_path.name, code, model)
    if not diff:
        print("No suggestions returned.")
        return

    print("\nSuggested changes:\n")
    print(diff)

    decision = prompt_user()

    if decision == "yes":
        write_diff(file_path, code, diff)
        print("\033[92mChanges applied.\033[0m")
    elif decision == "no":
        print("\033[93mSkipped.\033[0m")
    elif decision == "cancel":
        print("\033[91mCancelled by user.\033[0m")
        sys.exit(0)


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Agentic AI Code Improver Tool")
    parser.add_argument("--dir", type=str, default=".", help="Directory to scan")
    parser.add_argument("--file_type", type=str, required=True,
                        help="Comma-separated list of file extensions (e.g., py,js,ts)")
    parser.add_argument("--model", type=str, default="gpt-4o", help="OpenAI model to use")

    args = parser.parse_args()

    path = Path(args.dir).resolve()
    if not path.exists():
        print(f"Directory '{args.dir}' does not exist.")
        sys.exit(1)

    extensions = [ext.strip().lower() for ext in args.file_type.split(",")]
    files = find_files(path, extensions)

    if not files:
        print("No matching files found.")
        return

    for file_path in files:
        process_file(file_path, args.model)


if __name__ == "__main__":
    main()
