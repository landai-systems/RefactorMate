from unittest.mock import patch
from utils.openai_utils import get_code_diff_suggestion
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))



@patch("openai.ChatCompletion.create")
def test_get_code_diff_suggestion(mock_create):
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message={"content": "--- original\n+++ new\n@@ -1 +1 @@\n-print('hello')\n+print('hi')"})
    ]
    mock_create.return_value = mock_response

    result = get_code_diff_suggestion("test.py", "print('hello')", "gpt-4o")
    assert "print('hi')" in result


@patch("openai.ChatCompletion.create", side_effect=Exception("API down"))
def test_openai_error_handling(mock_create):
    result = get_code_diff_suggestion("test.py", "print('x')", "gpt-4o")
    assert result is None
