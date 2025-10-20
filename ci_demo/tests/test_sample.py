# ci_demo/tests/test_sample.py
import unittest
from fichier import addition

class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addition(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
