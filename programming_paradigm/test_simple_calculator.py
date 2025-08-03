import unittest
from simple_calculator.py import SimpleCalculator

class Test_Calculator(unittest.TestCase):
     def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(9,2), 7)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
if __name__ == "__main__":
  unittest.main()
