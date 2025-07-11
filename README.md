# 🛠️ RefactorMate

RefactorMate is a command-line tool that uses OpenAI's GPT models to automatically review and suggest improvements to source code files. It scans a directory for specified file types, sends their contents to OpenAI, and provides suggested changes in unified diff format. The user can then interactively apply or skip each proposed change.

---

## ✨ Features

- Supports multiple file extensions (`.py`, `.js`, `.ts`, etc.)
- Uses OpenAI GPT-4o or other ChatCompletion-compatible models
- Outputs human-readable code improvements in `diff` format
- User-controlled changes (`yes`, `no`, `cancel`)
- Logs all actions to a file (`agentic_ai.log`)
- Modular, testable and follows clean code principles

---

## 📦 Installation

```bash
git clone https://github.com/yourname/refactormate.git
cd refactormate

# Optional: use a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

---

## 🔐 Setup

Create a `.env` file in the root directory with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_key_here
```

Alternatively, you can set the key as an environment variable directly:

```bash
export OPENAI_API_KEY=your_openai_key_here
```

---

## 🚀 Usage

```bash
python main.py --dir ./src --file_type py,js --model gpt-4o
```

### Arguments

| Argument       | Description                                           |
|----------------|-------------------------------------------------------|
| `--dir`        | Directory to scan (default: current directory)        |
| `--file_type`  | Comma-separated list of file extensions to process    |
| `--model`      | OpenAI model to use (default: `gpt-4o`)               |

---

## 🧠 How it works

1. Recursively scans all files in the specified directory.
2. Filters by the given file types.
3. For each file:
    - Sends the file content to OpenAI with a prompt.
    - Receives a `diff` with proposed changes.
    - Displays the diff and asks user whether to apply, skip, or cancel.
    - If `yes`, the changes are written to the file.

---

## 📝 Example Session

```bash
$ python main.py --file_type py

Analyzing utils/core.py...

Suggested changes:

--- original.py
+++ improved.py
@@ -1,5 +1,6 @@
 import sys
+import logging
 from pathlib import Path
...

Apply changes? [yes/no/cancel]:
```

---

## 📁 Project Structure

```
refactormate/
├── main.py
├── .env
├── agentic_ai.log
├── requirements.txt
├── README.md
├── utils/
│   ├── __init__.py
│   ├── cli_utils.py
│   ├── core.py
│   ├── file_utils.py
│   └── openai_utils.py
└── tests/
    └── test_core.py
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🧰 Development Tools (Optional)

To format and type-check your code:

```bash
black .
mypy utils/
```

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. Contributions should follow best practices and clean code principles.

---

## 📬 Contact

Maintained by [Land AI](https://github.com/landai-systems).
