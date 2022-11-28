import unittest
import test

class Testmath(unittest.TestCase):

    def test_add(self):
        result = test.add(10, 10)
        result1 = test.add(5, 10)
        self.assertEqual(result, 20)
        self.assertEqual(result1, 15)

    def test_add1(self):
        result = test.add(10, 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()