import unittest

from anagram import is_anagram


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_anagram(self):
        self.assertEqual(is_anagram("silent","listen" ), True)
        self.assertEqual(is_anagram("sile", "listen"), False)
        self.assertEqual(is_anagram("silenx", "listen"), False)
        self.assertEqual(is_anagram("", "listen"), False)
        self.assertEqual(is_anagram("", ""), True)


if __name__ == '__main__':
    unittest.main()
