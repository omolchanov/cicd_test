import unittest

from src.main import get_random_int


class TestGetRandomFunction(unittest.TestCase):
    def test_get_random_int(self):
        self.assertIsInstance(get_random_int(), int)


if __name__ == '__main__':
    unittest.main()
