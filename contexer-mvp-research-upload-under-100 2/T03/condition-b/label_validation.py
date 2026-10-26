"""User-supplied label validation for the T03 fixture."""


def validate_label(label: str) -> str:
    """Validate and return a user-supplied label."""
    if not label.strip():
        raise ValueError("label must contain a non-whitespace character")
    return label
