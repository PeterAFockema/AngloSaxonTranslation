import unittest

from anglosaxon.langs import return_Langs_object

class TestLangs(unittest.TestCase):

    def test_return_Langs_object(self):
        return_Langs_object(self, "test")

if __name__ == '__main__':
    unittest.main()
