import unittest

from anglosaxon.string_manipulation import unicodeToAscii
from anglosaxon.string_manipulation import normaliseString

class TestFunctions(unittest.TestCase):

    def test_unicodeToAscii(self):
        self.assertEqual("123", unicodeToAscii("123"))

    def test_normaliseString_with_space_expected(self):
        self.assertEqual("a !", normaliseString("a123! "))

    def test_normaliseString_with_special_character(self):
        self.assertEqual("!", normaliseString("123! "))
    
    def test_normaliseString3_for_letters_only(self):
        self.assertEqual("a", normaliseString("a123 "))

if __name__ == '__main__':
    unittest.main()
