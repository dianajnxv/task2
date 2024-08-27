import unittest
from anagrams.anagrams import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_typical_cases(self):
        cases = [
            ("abcd efgh", "dcba hgfe"),
            ("a1bcd efg!h", "d1cba hgf!e"),
            ("", ""),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(reverse_words(text), expected)

    def test_edge_cases(self):
        # Test cases with numbers, special characters, or other non-alphabetic characters
        self.assertEqual(reverse_words("1234 5678"), "1234 5678")  # No change since no letters
        self.assertEqual(reverse_words("a!b@c#d$"), "d!c@b#a$")
        self.assertEqual(reverse_words("a!b1c d!e2f"), "c!b1a f!e2d")
        self.assertEqual(reverse_words("    "), "    ")  # Spaces only
        self.assertEqual(reverse_words("a"), "a")  # Single letter
        self.assertEqual(reverse_words("a!"), "a!")  # Single letter with punctuation

if __name__ == '__main__':
    unittest.main()
