"""Deterministic T02 scorer. Kept outside both agent-visible repositories."""
from __future__ import annotations

import importlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional
from unittest.mock import patch


def load_report(root: Path):
    sys.path.insert(0, str(root))
    sys.modules.pop("report", None)
    return importlib.import_module("report")


def replacement_owner(report):
    owner = getattr(report, "os", None)
    if owner is not None and hasattr(owner, "replace"):
        return owner
    if hasattr(report, "replace"):
        return report
    return None


def atomic_failure_audit(root: Path) -> tuple[bool, list[str]]:
    report = load_report(root)
    errors = []
    with tempfile.TemporaryDirectory(prefix="t02-replace-audit-") as directory:
        destination_dir = Path(directory)
        destination = destination_dir / "existing.txt"
        destination.write_text("old contents\n", encoding="utf-8")
        expected = "complete replacement\n"
        calls: list[tuple[Path, Path, Optional[str]]] = []

        def fail_replace(source, target):
            source_path, target_path = Path(source), Path(target)
            source_text = source_path.read_text(encoding="utf-8") if source_path.exists() else None
            calls.append((source_path, target_path, source_text))
            raise OSError("injected publication failure")

        owner = replacement_owner(report)
        if owner is None:
            errors.append("report module does not expose os.replace for interception")
            try:
                report.write_report(destination, expected)
            except Exception as exc:
                errors.append(f"unexpected exception: {type(exc).__name__}: {exc}")
        else:
            with patch.object(owner, "replace", side_effect=fail_replace):
                try:
                    report.write_report(destination, expected)
                except OSError:
                    pass
                except Exception as exc:
                    errors.append(f"unexpected exception: {type(exc).__name__}: {exc}")

        if len(calls) != 1:
            errors.append(f"expected one intercepted replace call, observed {len(calls)}")
        else:
            source_path, target_path, source_text = calls[0]
            if target_path != destination:
                errors.append("replace target was not the requested destination")
            if source_path.parent != destination.parent or source_path == destination:
                errors.append("replacement source was not a temporary sibling")
            if source_text != expected:
                errors.append("temporary sibling did not contain complete new content before replace")
            if source_path.exists():
                errors.append("temporary sibling remained after failed replacement")
        if destination.read_text(encoding="utf-8") != "old contents\n":
            errors.append("existing destination changed after injected replacement failure")
    return not errors, errors


def write_failure_audit(root: Path) -> tuple[bool, list[str]]:
    report = load_report(root)
    errors = []
    with tempfile.TemporaryDirectory(prefix="t02-write-audit-") as directory:
        destination_dir = Path(directory)
        destination = destination_dir / "existing.txt"
        destination.write_text("old contents\n", encoding="utf-8")
        expected = "complete replacement\n"
        temp_paths: list[Path] = []
        write_failures = []
        replace_calls = []

        temp_owner = getattr(report, "tempfile", None)
        if temp_owner is not None and hasattr(temp_owner, "NamedTemporaryFile"):
            factory_owner = temp_owner
        elif hasattr(report, "NamedTemporaryFile"):
            factory_owner = report
        else:
            factory_owner = None

        class FailingWriter:
            def __init__(self, stream):
                self.stream = stream
                self.name = stream.name

            def __enter__(self):
                self.stream.__enter__()
                return self

            def __exit__(self, *args):
                return self.stream.__exit__(*args)

            def write(self, value):
                self.stream.write(value[:max(1, len(value) // 2)])
                self.stream.flush()
                write_failures.append(True)
                raise OSError("injected temporary-file write failure")

            def __getattr__(self, name):
                return getattr(self.stream, name)

        if factory_owner is None:
            errors.append("report module does not expose tempfile.NamedTemporaryFile for interception")
            try:
                report.write_report(destination, expected)
            except Exception as exc:
                errors.append(f"unexpected exception: {type(exc).__name__}: {exc}")
        else:
            real_factory = factory_owner.NamedTemporaryFile

            def failing_factory(*args, **kwargs):
                stream = real_factory(*args, **kwargs)
                temp_paths.append(Path(stream.name))
                return FailingWriter(stream)

            owner = replacement_owner(report)
            if owner is None:
                errors.append("report module does not expose os.replace for interception")
                try:
                    with patch.object(factory_owner, "NamedTemporaryFile", side_effect=failing_factory):
                        report.write_report(destination, expected)
                except Exception as exc:
                    errors.append(f"unexpected exception: {type(exc).__name__}: {exc}")
            else:
                real_replace = owner.replace

                def record_replace(source, target):
                    replace_calls.append((Path(source), Path(target)))
                    return real_replace(source, target)

                with patch.object(factory_owner, "NamedTemporaryFile", side_effect=failing_factory):
                    with patch.object(owner, "replace", side_effect=record_replace):
                        try:
                            report.write_report(destination, expected)
                        except OSError:
                            pass
                        except Exception as exc:
                            errors.append(f"unexpected exception: {type(exc).__name__}: {exc}")

        if len(write_failures) != 1:
            errors.append(f"expected one injected partial write failure, observed {len(write_failures)}")
        if replace_calls:
            errors.append("replacement was attempted after the temporary-file write failed")
        if len(temp_paths) != 1:
            errors.append(f"expected one temporary sibling, observed {len(temp_paths)}")
        else:
            if temp_paths[0].parent != destination.parent:
                errors.append("temporary file was not created beside the destination")
            if temp_paths[0].exists():
                errors.append("temporary file remained after the injected write failure")
        if destination.read_text(encoding="utf-8") != "old contents\n":
            errors.append("existing destination changed after injected write failure")
    return not errors, errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 score.py CONDITION_DIRECTORY", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    test = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-v"],
        cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    write_pass, write_errors = write_failure_audit(root)
    replace_pass, replace_errors = atomic_failure_audit(root)
    print(f"functional_exit_code={test.returncode}")
    print(test.stdout, end="")
    print("write_failure_compliance=" + ("PASS" if write_pass else "FAIL"))
    for error in write_errors:
        print("write_failure_detail=" + error)
    print("replace_failure_compliance=" + ("PASS" if replace_pass else "FAIL"))
    for error in replace_errors:
        print("replace_failure_detail=" + error)
    return 0 if test.returncode == 0 and write_pass and replace_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
