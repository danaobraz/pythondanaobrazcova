import unittest


class Calculator:
    def add(self, a, b):
        return a + b


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


if __name__ == '__main__':
    unittest.main()
