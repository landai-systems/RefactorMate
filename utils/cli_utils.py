def prompt_user() -> str:
    """
    Prompt the user for a decision on applying a change.

    Returns:
        str: 'yes', 'no', or 'cancel'
    """
    while True:
        response = input("\nApply changes? [yes/no/cancel]: ").strip().lower()
        if response in ("yes", "no", "cancel"):
            return response
        print("Invalid input. Please enter 'yes', 'no', or 'cancel'.")