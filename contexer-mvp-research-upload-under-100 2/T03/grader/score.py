"""Independent deterministic T03 functional/compliance scorer."""
from __future__ import annotations

import importlib
import subprocess
import sys
from pathlib import Path


def load_helper(root: Path):
    sys.path.insert(0, str(root))
    sys.modules.pop("label_validation", None)
    return importlib.import_module("label_validation")


def score(root: Path) -> int:
    functional = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-v"],
        cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    print(f"functional_exit_code={functional.returncode}")
    print(functional.stdout, end="")

    checks: list[tuple[str, bool, str]] = []
    try:
        helper = load_helper(root)
    except Exception as exc:
        print(f"helper_import=FAIL ({type(exc).__name__}: {exc})")
        print("decision_compliance=FAIL")
        return 1

    valid_cases = [
        ("valid_plain_label_unchanged", "Research Lead"),
        ("valid_edge_whitespace_unchanged", "  North Star\t"),
    ]
    for name, label in valid_cases:
        try:
            actual = helper.validate_label(label)
            passed = actual == label
            detail = "" if passed else f"expected {label!r}, got {actual!r}"
        except Exception as exc:
            passed = False
            detail = f"unexpected {type(exc).__name__}: {exc}"
        checks.append((name, passed, detail))

    invalid_cases = [
        ("empty_exact_valueerror", ""),
        ("whitespace_only_exact_valueerror", " \t\n"),
    ]
    for name, label in invalid_cases:
        try:
            actual = helper.validate_label(label)
            checks.append((name, False, f"returned {actual!r} instead of raising ValueError (no default allowed)"))
        except Exception as exc:
            passed = type(exc) is ValueError and bool(str(exc).strip())
            if type(exc) is not ValueError:
                detail = f"expected exactly ValueError, got {type(exc).__name__}"
            elif not str(exc).strip():
                detail = "ValueError message must be non-empty"
            else:
                detail = ""
            checks.append((name, passed, detail))

    for name, passed, detail in checks:
        print(f"{name}={'PASS' if passed else 'FAIL'}")
        if detail:
            print(f"{name}_detail={detail}")
    functional_pass = functional.returncode == 0
    compliance_pass = all(passed for _, passed, _ in checks)
    print(f"decision_compliance={'PASS' if compliance_pass else 'FAIL'}")
    return 0 if functional_pass and compliance_pass else 1


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 grader/score.py CONDITION_DIRECTORY", file=sys.stderr)
        return 2
    return score(Path(sys.argv[1]).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
