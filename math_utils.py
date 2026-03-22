class MyMath:
    @staticmethod
    def add(a, b):
        """Сложение двух чисел(целочисленные или с плавающей точкой).

        Args:
            a - первое число,
            b - второе число.

        Returns:
            a + b - сумма a и b.

        Raises:
            TypeError - если введенные аргументы не числа.
        """

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ввести можно только целые числа или числа с плавающей точкой!")

        return a + b

    @staticmethod
    def subtract(a, b):
        """Вычитание второго числа из первого(целочисленные или с плавающей точкой).

        Args:
            a - уменьшаемое число,
            b - вычитаемое число.

        Returns:
            a - b - разность a и b.

        Raises:
            TypeError - если введенные аргументы не числа.
        """

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ввести можно только целые числа или числа с плавающей точкой!")

        return a - b

    @staticmethod
    def multiply(a, b):
        """Умножение двух чисел(целочисленные или с плавающей точкой).

        Args:
            a - первый множитель,
            b - второй множитель.

        Returns:
            a * b - произведение a и b.

        Raises:
            TypeError - если введенные аргументы не числа.
        """

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ввести можно только целые числа или числа с плавающей точкой!")

        return a * b

    @staticmethod
    def divide(a, b):
        """Деление первого числа на второе(целочисленные или с плавающей точкой).

        Args:
            a - делимое,
            b - делитель.

        Returns:
            a / b - частное от деления a на b.

        Raises:
            TypeError - если введенные аргументы не числа.
            ZeroDivisionError - если делитель равен 0.
        """

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ввести можно только целые числа или числа с плавающей точкой!")
        elif b == 0:
            raise ZeroDivisionError("Нельзя делить на 0!")

        return a / b
