from unittest.mock import patch
from utils.cli_utils import prompt_user
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


@patch("builtins.input", return_value="yes")
def test_prompt_user_yes(mock_input):
    assert prompt_user() == "yes"


@patch("builtins.input", side_effect=["maybe", "no"])
def test_prompt_user_invalid_then_no(mock_input):
    assert prompt_user() == "no"
