import pytest

from math_utils import (
    MyMath,
)


class TestAdd:
    """Тесты для функции сложения(add)."""

    @pytest.mark.feature('add')
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 8),
        (-5, -3, -8),
        (5, -3, 2),
    ])
    def test_add_int(self, a, b, expected):
        """Тест-1: сложение целых чисел."""
        assert MyMath.add(a, b) == expected

    @pytest.mark.feature('add')
    @pytest.mark.parametrize("a,b,expected", [
        (2.5, 3.7, 6.2),
        (3.3, -2.2, 1.1),
    ])
    def test_add_floats(self, a, b, expected):
        """Тест-2: сложение чисел с плавающей точкой."""
        assert MyMath.add(a, b) == pytest.approx(expected)

    @pytest.mark.feature('add')
    def test_add_mixed_types(self):
        """Тест-3: сложение целого числа и числа с плавающей точкой."""

        assert MyMath.add(5, 2.5) == 7.5

    @pytest.mark.feature('add')
    def test_add_type_error(self):
        """Тест-4: ошибка наличия нечислового значения среди входных параметров."""

        with pytest.raises(TypeError):
            MyMath.add('a', 3)


class TestSubtract:
    """Тестовые случаи для функции вычитания(subtract)."""

    @pytest.mark.feature('subtract')
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 2),
        (-3, -5, 2),
        (5, -3, 8),
    ])
    def test_subtract_int(self, a, b, expected):
        """Тест-1: вычитание целых чисел."""

        assert MyMath.subtract(a, b) == expected

    @pytest.mark.feature('subtract')
    @pytest.mark.parametrize("a,b,expected", [
        (10.5, 3.2, 7.3),
        (-5.2, -3.4, -1.8),
        (5.3, -3.8, 9.1),
    ])
    def test_subtract_float(self, a, b, expected):
        """Тест-2: вычитание чисел с плавающей точкой."""

        assert MyMath.subtract(a, b) == pytest.approx(expected)

    @pytest.mark.feature('subtract')
    def test_subtract_with_zero(self):
        """Тест-3: вычитание с нулём."""

        assert MyMath.subtract(5, 0) == 5

    @pytest.mark.feature('subtract')
    def test_subtract_second_larger(self):
        """Тест-4: вычитание, где второе число больше."""

        assert MyMath.subtract(5, 10) == -5

    @pytest.mark.feature('subtract')
    def test_subtract_type_error(self):
        """Тест-5: ошибка наличия нечислового значения среди входных параметров."""

        with pytest.raises(TypeError):
            MyMath.subtract('a', 3)


class TestMultiply:
    """Тестовые случаи для функции умножения(multiply)."""

    @pytest.mark.feature('multiply')
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 15),
        (-3, 5, -15),
        (-5, -3, 15),
    ])
    def test_multiply_int(self, a, b, expected):
        """Тест-1: умножение целых чисел."""

        assert MyMath.multiply(a, b) == expected

    @pytest.mark.feature('multiply')
    def test_multiply_with_zero(self):
        """Тест-2: умножение с нулём."""

        assert MyMath.multiply(5, 0) == 0

    @pytest.mark.feature('multiply')
    def test_multiply_floats(self):
        """Тест-3: умножение чисел с плавающей точкой."""

        assert MyMath.multiply(2.5, 3.5) == 8.75

    @pytest.mark.feature('multiply')
    def test_multiply_with_one(self):
        """Тест-4: умножение на единицу."""

        assert MyMath.multiply(5, 1) == 5

    @pytest.mark.feature('multiply')
    def test_multiply_type_error(self):
        """Тест-5: ошибка наличия нечислового значения среди входных параметров."""

        with pytest.raises(TypeError):
            MyMath.multiply('a', 3)


class TestDivide:
    """Тестовые случаи для функции деления(divide)."""

    @pytest.mark.feature('divide')
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),
    ])
    def test_divide_int(self, a, b, expected):
        """Тест-1: деление целых чисел."""

        assert MyMath.divide(a, b) == expected

    @pytest.mark.feature('divide')
    def test_divide_resulting_float(self):
        """Тест-2: деление с результатом в виде числа с плавающей точкой."""

        assert MyMath.divide(10, 3) == 3.3333333333333335

    @pytest.mark.feature('divide')
    def test_divide_floats(self):
        """Тест-3: деление чисел с плавающей точкой."""

        assert MyMath.divide(10.5, 2.5) == 4.2

    @pytest.mark.feature('divide')
    def test_divide_by_zero(self):
        """Тест-4: деление на ноль."""

        with pytest.raises(ZeroDivisionError):
            MyMath.divide(10, 0)

    @pytest.mark.feature('divide')
    def test_divide_zero(self):
        """Тест-5: деление, где делимое равно нулю."""

        assert MyMath.divide(0, 5) == 0.0

    @pytest.mark.feature('divide')
    def test_divide_type_error(self):
        """Тест-6: ошибка наличия нечислового значения среди входных параметров."""

        with pytest.raises(TypeError):
            MyMath.divide('a', 2)
