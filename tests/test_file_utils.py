import tempfile
from pathlib import Path
from utils.file_utils import read_file, write_diff, find_files
import sys
import difflib
sys.path.append(str(Path(__file__).resolve().parents[1]))



def test_read_and_write_file():
    original = "print('hello')"
    modified = "print('hello world')"
    diff = "\n".join(difflib.ndiff(original.splitlines(), modified.splitlines()))

    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.py"
        file_path.write_text(original)

        write_diff(file_path, original, diff)
        new_content = read_file(file_path)
        assert "hello world" in new_content


def test_find_files(tmp_path):
    (tmp_path / "a.py").write_text("print('A')")
    (tmp_path / "b.js").write_text("console.log('B');")
    (tmp_path / "c.txt").write_text("text")

    found = find_files(tmp_path, ["py", "js"])
    found_names = [f.name for f in found]
    assert "a.py" in found_names
    assert "b.js" in found_names
    assert "c.txt" not in found_names
