import unittest

from src.main import *


class TestGetRandomFunction(unittest.TestCase):

    def test_get_random_int(self):
        self.assertIsInstance(get_random_int(), int)

    def test_get_random_float(self):
        self.assertIsInstance(get_random_float(), float)

    def test_get_random_string(self):
        """
        Test
        :return:
        """
        self.assertIsInstance(get_random_string(), str)


if __name__ == '__main__':
    unittest.main()
