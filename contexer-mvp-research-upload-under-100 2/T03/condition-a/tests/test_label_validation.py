import unittest

from label_validation import validate_label


class LabelValidationTests(unittest.TestCase):
    def test_returns_ordinary_label_unchanged(self):
        self.assertEqual(validate_label("Research Lead"), "Research Lead")

    def test_preserves_whitespace_on_nonblank_label(self):
        label = "  North Star\t"
        self.assertEqual(validate_label(label), label)

    def test_rejects_empty_label(self):
        with self.assertRaises(ValueError):
            validate_label("")

    def test_rejects_whitespace_only_label(self):
        with self.assertRaises(ValueError):
            validate_label(" \t\n")

    def test_rejects_non_string_label(self):
        with self.assertRaises(TypeError):
            validate_label(None)


if __name__ == "__main__":
    unittest.main()
