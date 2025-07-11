from unittest.mock import patch, MagicMock
from utils.core import process_file
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))


@patch("utils.core.read_file", return_value="print('x')")
@patch("utils.core.get_code_diff_suggestion", return_value="--- \n+++ \n@@ -1 +1 @@\n-print('x')\n+print('y')")
@patch("utils.core.prompt_user", return_value="yes")
@patch("utils.core.write_diff")
def test_process_file_applies_diff(mock_write, mock_prompt, mock_diff, mock_read):
    process_file(Path("dummy.py"), "gpt-4o")
    mock_write.assert_called_once()
