import unittest
from math_utils import (
    MyMath,
)


class TestAdd(unittest.TestCase):
    """Тесты для функции сложения(add)."""

    def test_add_int(self):
        """Тест-1: сложение целых чисел."""

        test_cases = [(5, 3, 8), (-5, -3, -8), (5, -3, 2)]
        for a, b, expected in test_cases:
            with self.subTest(a, b=b, expected=expected):
                self.assertEqual(MyMath.add(a, b), expected)

    def test_add_floats(self):
        """Тест-2: сложение чисел с плавающей точкой."""

        test_cases = [(2.5, 3.7, 6.2), (3.3, -2.2, 1.1)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertAlmostEqual(MyMath.add(a, b), expected)

    def test_add_mixed_types(self):
        """Тест-3: сложение целого числа и числа с плавающей точкой."""

        self.assertAlmostEqual(MyMath.add(5, 2.5), 7.5)

    def test_add_type_error(self):
        """Тест-4: ошибка наличия нечислового значения среди входных параметров."""

        with self.assertRaises(TypeError):
            MyMath.add('a', 3)


class TestSubtract(unittest.TestCase):
    """Тестовые случаи для функции вычитания(subtract)."""

    def test_subtract_int(self):
        """Тест-1: вычитание целых чисел."""

        test_cases = [(5, 3, 2), (-3, -5, 2), (5, -3, 8)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(MyMath.subtract(a, b), expected)

    def test_subtract_float(self):
        """Тест-2: Вычитание чисел с плавающей точкой."""

        test_cases = [(10.5, 3.2, 7.3), (-5.2, -3.4, -1.8), (5.3, -3.8, 9.1)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(MyMath.subtract(a, b), expected)

    def test_subtract_with_zero(self):
        """Тест-3: вычитание с нулём."""

        self.assertEqual(MyMath.subtract(5, 0), 5)

    def test_subtract_second_larger(self):
        """Тест-4: вычитание, где второе число больше."""

        self.assertEqual(MyMath.subtract(5, 10), -5)

    def test_subtract_type_error(self):
        """Тест-5: ошибка наличия нечислового значения среди входных параметров."""

        with self.assertRaises(TypeError):
            MyMath.subtract('a', 3)


class TestMultiply(unittest.TestCase):
    """Тестовые случаи для функции умножения(multiply)."""

    def test_multiply_int(self):
        """Тест-1: умножение целых чисел."""

        test_cases = [(5, 3, 15), (-3, 5, -15), (-5, -3, 15)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(MyMath.multiply(a, b), expected)

    def test_multiply_with_zero(self):
        """Тест-2: умножение с нулём."""

        self.assertEqual(MyMath.multiply(5, 0), 0)

    def test_multiply_floats(self):
        """Тест-3: умножение чисел с плавающей точкой."""

        self.assertAlmostEqual(MyMath.multiply(2.5, 3.5), 8.75)

    def test_multiply_with_one(self):
        """Тест-4: умножение на единицу."""

        self.assertEqual(MyMath.multiply(5, 1), 5)

    def test_multiply_type_error(self):
        """Тест-5: ошибка наличия нечислового значения среди входных параметров."""

        with self.assertRaises(TypeError):
            MyMath.multiply('a', 3)


class TestDivide(unittest.TestCase):
    """Тестовые случаи для функции деления(divide)."""

    def test_divide_int(self):
        """Тест-1: деление целых чисел."""

        test_cases = [(10, 2, 5.0), (10, -2, -5.0), (-10, -2, 5.0)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(MyMath.divide(a, b), expected)

    def test_divide_resulting_float(self):
        """Тест-2: деление с результатом в виде числа с плавающей точкой."""

        self.assertAlmostEqual(MyMath.divide(10, 3), 3.3333333333333335)

    def test_divide_floats(self):
        """Тест-3: деление чисел с плавающей точкой."""

        self.assertAlmostEqual(MyMath.divide(10.5, 2.5), 4.2)

    def test_divide_by_zero(self):
        """Тест-4: деление на ноль."""

        with self.assertRaises(ZeroDivisionError):
            MyMath.divide(10, 0)

    def test_divide_zero(self):
        """Тест-5: деление, где делимое равно нулю."""

        self.assertEqual(MyMath.divide(0, 5), 0.0)

    def test_divide_type_error(self):
        """Тест-6: ошибка наличия нечислового значения среди входных параметров."""

        with self.assertRaises(TypeError):
            MyMath.divide('a', 2)


if __name__ == "__main__":
    unittest.main()
