import openai
from typing import Optional
import os

PROMPT_TEMPLATE = """
You are an expert code reviewer. The user will provide the filename and full content of a source code file.

You will respond with a unified diff (like from `diff -u`) showing improvements and cleanups to the code.
Only return the diff.

Filename: {filename}

Content:
{content}
""" 


def get_code_diff_suggestion(filename: str, content: str, model: str) -> Optional[str]:
    """
    Query the OpenAI model to get improvement suggestions as a diff.

    Args:
        filename (str): Name of the file.
        content (str): File content.
        model (str): OpenAI model name.

    Returns:
        Optional[str]: Suggested diff or None.
    """
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful code improvement assistant."},
                {"role": "user", "content": PROMPT_TEMPLATE.format(filename=filename, content=content)}
            ],
            temperature=0.3,
            max_tokens=1024
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        # Fehler wird im aufrufenden Modul geloggt
        return None
