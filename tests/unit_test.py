import unittest
from anagrams.anagrams import reverse_word, reverse_words

class TestAnagrams(unittest.TestCase):

    def test_reverse_word_typical(self):
        self.assertEqual(reverse_word("abcd"), "dcba")
        self.assertEqual(reverse_word("a1bcd"), "d1cba")
        self.assertEqual(reverse_word("a!b@c#d$"), "d!c@b#a$")
        self.assertEqual(reverse_word(""), "")

    def test_reverse_words_typical(self):
        self.assertEqual(reverse_words("abcd efgh"), "dcba hgfe")
        self.assertEqual(reverse_words("a1bcd efg!h"), "d1cba hgf!e")
        self.assertEqual(reverse_words(""), "")

    def test_reverse_word_edge_cases(self):
        self.assertEqual(reverse_word("1234"), "1234")
        self.assertEqual(reverse_word("!@#$"), "!@#$")
        self.assertEqual(reverse_word("a"), "a")
        self.assertEqual(reverse_word("a!"), "a!")

    def test_reverse_words_edge_cases(self):
        self.assertEqual(reverse_words("1234 5678"), "1234 5678")
        self.assertEqual(reverse_words("a!b1c d!e2f"), "c!b1a f!e2d")
        self.assertEqual(reverse_words("    "), "    ")

if __name__ == '__main__':
    unittest.main()
