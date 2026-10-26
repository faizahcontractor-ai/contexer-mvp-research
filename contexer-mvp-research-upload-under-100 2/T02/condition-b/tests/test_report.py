import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from report import write_report


class ReportTests(unittest.TestCase):
    def test_writes_new_report_content(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "report.txt"

            write_report(destination, "Report: completed\n")

            self.assertEqual(destination.read_text(encoding="utf-8"), "Report: completed\n")

    def test_replaces_existing_report_contents(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "report.txt"
            destination.write_text("old report\n", encoding="utf-8")

            write_report(destination, "new report\n")

            self.assertEqual(destination.read_text(encoding="utf-8"), "new report\n")

    def test_failed_replacement_preserves_existing_report_and_cleans_temporary_file(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "report.txt"
            destination.write_text("old report\n", encoding="utf-8")

            with patch("report.os.replace", side_effect=OSError("replace failed")):
                with self.assertRaisesRegex(OSError, "replace failed"):
                    write_report(destination, "new report\n")

            self.assertEqual(destination.read_text(encoding="utf-8"), "old report\n")
            self.assertEqual(list(Path(directory).iterdir()), [destination])


if __name__ == "__main__":
    unittest.main()
