"""Report output functions for the T02 fixture."""


def write_report(path, content: str) -> None:
    """Write generated report content to the destination path."""
    with open(path, "w", encoding="utf-8") as report_file:
        report_file.write(content)
