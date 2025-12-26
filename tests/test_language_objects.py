import unittest

from anglosaxon.language_objects import return_value

class TestLanguageObjects(unittest.TestCase):

    def test_return_value(self):
        return_value(1,2)

if __name__ == '__main__':
    unittest.main()
