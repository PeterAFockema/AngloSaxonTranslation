import unittest

from anglosaxon.functions import add

class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(11, add(5, 6))

if __name__ == '__main__':
    unittest.main()
