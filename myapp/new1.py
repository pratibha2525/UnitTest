import unittest
from number import evenn

class TestEvenOdd(unittest.TestCase):

    def test_even(self):
        self.assertTrue(evenn(30))
        self.assertFalse(evenn(9))


if __name__ == '__main__':
    unittest.main()