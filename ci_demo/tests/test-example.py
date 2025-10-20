# ci_demo/tests/test_sample.py
import unittest
from fichier import addition, multiplication

class TestCalculs(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)
        self.assertEqual(multiplication(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
