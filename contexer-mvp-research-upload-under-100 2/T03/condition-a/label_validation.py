"""User-supplied label validation for the T03 fixture."""


def validate_label(label: str) -> str:
    """Validate and return a user-supplied label."""
    if not isinstance(label, str):
        raise TypeError("label must be a string")
    if not label.strip():
        raise ValueError("label must not be blank")
    return label
