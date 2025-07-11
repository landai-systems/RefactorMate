import openai
from typing import Optional
import os
import logging


PROMPT_TEMPLATE = """
You are an expert Python software architect.

Your task is to refactor the provided code to improve:
- readability
- modularity (split into functions if needed)
- performance
- naming conventions (PEP8)
- remove dead code or bad patterns

Return only the unified diff (diff -u style).

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
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful code improvement assistant."},
                {"role": "user", "content": PROMPT_TEMPLATE.format(filename=filename, content=content)}
            ],
            temperature=0.3,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        # Fehler wird im aufrufenden Modul geloggt
        logging.error(f"OpenAI API call failed: {e}")
        return None
