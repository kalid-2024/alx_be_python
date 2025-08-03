import unittest
from simple_calculator.py import SimpleCalculator

class Test_Calculator(unittest.TestCase):
     def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add_positive(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative(self):
        result = self.calc.add(-2, 7)
        self.assertEqual(result, 5)

    def test_subtract_postive(self):
        result = self.calc.subtract(9,2)
        self.assertEqual(result, 7)

    def test_subtract_negative(self):
        result = self.calc.subtract(-9,2)
        self.assertEqual(result, -11)
    
    def test_multiply_positive(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_multiply_negative(self):
        result = self.calc.multiply(-4, 2)
        self.assertEqual(result, -8)

    def test_divide_normal(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_negative(self):
        result = self.calc.divide(-10, 2)
        self.assertEqual(result, -5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
if __name__ == "__main__":
  unittest.main()
