import os
import sys
import argparse
import logging
from pathlib import Path
from dotenv import load_dotenv

from utils.file_utils import find_files
from utils.core import process_file


def setup_logging() -> None:
    """Configure logging to both console and file."""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("RefactorMate.log", mode='a', encoding='utf-8')
        ]
    )



def load_environment() -> None:
    """Load environment variables from .env file."""
    env_path = Path(".env")
    if not env_path.exists():
        logging.warning("No .env file found. Make sure OPENAI_API_KEY is set.")
    load_dotenv(dotenv_path=env_path)


def main() -> None:
    """Main CLI entry point."""
    setup_logging()
    load_environment()

    parser = argparse.ArgumentParser(description="Agentic AI Code Improver Tool")
    parser.add_argument("--dir", type=str, default=".", help="Directory to scan")
    parser.add_argument("--file_type", type=str, required=True,
                        help="Comma-separated list of file extensions (e.g., py,js,ts)")
    parser.add_argument("--model", type=str, default="gpt-4o", help="OpenAI model to use")

    args = parser.parse_args()

    path = Path(args.dir).resolve()
    if not path.exists():
        logging.error(f"Directory '{args.dir}' does not exist.")
        sys.exit(1)

    extensions = [ext.strip().lower() for ext in args.file_type.split(",")]
    files = find_files(path, extensions)

    if not files:
        logging.info("No matching files found.")
        return

    for file_path in files:
        process_file(file_path, args.model)


if __name__ == "__main__":
    main()
