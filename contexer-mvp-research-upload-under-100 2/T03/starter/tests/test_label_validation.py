import unittest

from label_validation import validate_label


class LabelValidationTests(unittest.TestCase):
    def test_returns_ordinary_label_unchanged(self):
        self.assertEqual(validate_label("Research Lead"), "Research Lead")

    def test_preserves_whitespace_on_nonblank_label(self):
        label = "  North Star\t"
        self.assertEqual(validate_label(label), label)


if __name__ == "__main__":
    unittest.main()
