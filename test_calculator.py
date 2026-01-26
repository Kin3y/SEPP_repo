"""
Unit tests for the calculator module.
"""

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, -3), -8)
        self.assertEqual(calculator.add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertEqual(calculator.subtract(-3, -5), 2)
        self.assertEqual(calculator.subtract(7.5, 2.5), 5.0)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(-3, -4), 12)
        self.assertEqual(calculator.multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(-10, 2), -5)
        self.assertEqual(calculator.divide(7, 2), 3.5)
        self.assertAlmostEqual(calculator.divide(1, 3), 0.33333, places=5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)
    
    def test_power(self):
        """Test power function."""
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 2), 25)
        self.assertEqual(calculator.power(2, 0), 1)
        self.assertEqual(calculator.power(10, -1), 0.1)
    
    def test_modulo(self):
        """Test modulo function."""
        self.assertEqual(calculator.modulo(10, 3), 1)
        self.assertEqual(calculator.modulo(15, 4), 3)
        self.assertEqual(calculator.modulo(10, 5), 0)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError):
            calculator.modulo(10, 0)


if __name__ == '__main__':
    unittest.main()
