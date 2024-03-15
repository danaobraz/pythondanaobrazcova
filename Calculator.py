
#git
class Calculator:
    pass
import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Arrange
        calculator = Calculator()
        a = 5
        b = 7

        # Act
        result = calculator.add(a, b)

        # Assert
        self.assertEqual(result, 12)

    def test_subtract(self):
        # Arrange
        calculator = Calculator()
        a = 10
        b = 3

        # Act
        result = calculator.subtract(a, b)

        # Assert
        self.assertEqual(result, 7)

    def test_multiply(self):
        # Arrange
        calculator = Calculator()
        a = 4
        b = 6

        # Act
        result = calculator.multiply(a, b)

        # Assert
        self.assertEqual(result, 24)

    def test_divide(self):
        # Arrange
        calculator = Calculator()
        a = 10
        b = 2

        # Act
        result = calculator.divide(a, b)

        # Assert
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        calculator = Calculator()
        a = 10
        b = 0
        with self.assertRaises(ValueError):
            calculator.divide(a, b)

if __name__ == '__main__':
    unittest.main()
class Calculator:
    def power(self, base, exponent):
        if base == 0 and exponent == 0:
            raise ArithmeticError("Indeterminate value: 0^0")
        return base ** exponent

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b) if a and b else 0

import unittest

class TestCalculator(unittest.TestCase):
    def test_power(self):
        calculator = Calculator()
        base = 2
        exponent = 3
        expected_result = 8
        result = calculator.power(base, exponent)
        self.assertEqual(result, expected_result)

    def test_power_zero_to_zero(self):
        calculator = Calculator()
        base = 0
        exponent = 0
        with self.assertRaises(ArithmeticError):
            calculator.power(base, exponent)

    def test_gcd(self):
        calculator = Calculator()
        a = 24
        b = 36
        expected_result = 12
        result = calculator.gcd(a, b)
        self.assertEqual(result, expected_result)

    def test_lcm(self):
        calculator = Calculator()
        a = 4
        b = 6
        expected_result = 12
        result = calculator.lcm(a, b)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
