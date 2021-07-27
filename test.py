import unittest
from unittest import TestCase, mock


class CITest(TestCase):
    def test_simple(self):
        a = 1
        self.assertEqual(1, a)
        print('hello, DroneCI')


if __name__ == "__main__":
    unittest.main()
