import sys
import logging
from pathlib import Path

from utils.cli_utils import prompt_user
from utils.file_utils import read_file, write_diff
from utils.openai_utils import get_code_diff_suggestion


def process_file(file_path: Path, model: str) -> None:
    """
    Process a single file: send content to OpenAI, get diff, prompt user, apply diff.

    Args:
        file_path (Path): Path to the code file to process.
        model (str): OpenAI model name to use.
    """
    logging.info(f"Analyzing {file_path}...")
    code = read_file(file_path)

    diff = get_code_diff_suggestion(file_path.name, code, model)
    if not diff:
        logging.info("No suggestions returned.")
        return

    print("\nSuggested changes:\n")
    print(diff)

    decision = prompt_user()

    if decision == "yes":
        write_diff(file_path, code, diff)
        logging.info(f"Changes applied to {file_path}.")
    elif decision == "no":
        logging.info(f"Skipped {file_path}.")
    elif decision == "cancel":
        logging.warning("Process cancelled by user.")
        sys.exit(0)
