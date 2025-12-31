import unittest

from anglosaxon.string_manipulation import unicodeToAscii
from anglosaxon.string_manipulation import normaliseString

class TestFunctions(unittest.TestCase):

    def test_unicodeToAscii(self):
        self.assertEqual(11, unicodeToAscii("123"))

    def test_normaliseString(self):
        self.assertEqual("123", normaliseString("123! "))

if __name__ == '__main__':
    unittest.main()
