import unittest
from src.app import add

class TestApp(unittest.TestCase):
    """
    Unit tests for the add function.
    """
    def test_add(self):
        # Test case 1: Positive numbers
        self.assertEqual(add(3, 5), 8)
        # Test case 2: Negative numbers
        self.assertEqual(add(-3, -5), -8)
        # Test case 3: Mixed numbers
        self.assertEqual(add(-3, 5), 2)
        # Test case 4: Floats
        self.assertAlmostEqual(add(3.1, 2.2), 5.3)

if __name__ == "__main__":
    unittest.main()
