"""Hometask 16_2."""

from abc import ABC, abstractmethod

"""
Створіть абстрактний клас "Фігура" з абстрактними методами
для отримання площі та периметру. Наслідуйте від нього
декілька (> 2) інших фігур, та реалізуйте математично вірні
для них методи для площі та периметру. Властивості по типу
“довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись
через конструктор. Створіть Декілька різних об’єктів фігур, та
у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Square(Shape):
    """Square class that represents a square shape."""

    def __init__(self, a):
        """
        Initialize the square with side length a.

        :param a: Length of the side of the square.
        """
        if a <= 0:
            raise ValueError('Side length must be positive.')
        self.__a = a

    def area(self):
        """Calculate the area of the square."""
        return self.__a * self.__a

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return self.__a * 4

    def get_args(self):
        """Return the parameters of the square."""
        return f'Side length: {self.__a}'


class Triangle(Shape):
    """Triangle class that represents a triangle shape."""

    def __init__(self, a, b, c, height):
        """
        Initialize the triangle with three sides and height.

        :param a: Base of the triangle.
        :param b: Second side of the triangle.
        :param c: Third side of the triangle.
        :param height: Height corresponding to the base.
        """
        if a <= 0 or b <= 0 or c <= 0 or height <= 0:
            raise ValueError('Sides and height must be positive.')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Invalid side lengths for a triangle.')
        self.__a = a
        self.__b = b
        self.__c = c
        self.__height = height

    def area(self):
        """Calculate the area of the triangle."""
        return (self.__a * self.__height) / 2

    def perimeter(self):
        """Calculate the perimeter of the triangle."""
        return self.__a + self.__b + self.__c

    def get_args(self):
        """Return the parameters of the triangle."""
        return (f'Sides: {self.__a}, {self.__b}, {self.__c}, '
                f'Height: {self.__height}')


if __name__ == '__main__':
    shapes = [
        Square(4),
        Square(7),
        Triangle(3, 4, 5, 2.5),
        Triangle(6, 8, 10, 4),
    ]

    for shape in shapes:
        print(f'Shape: {type(shape).__name__}')
        print(f'  Parameters: {shape.get_args()}')
        print(f'  Area: {shape.area()}')
        print(f'  Perimeter: {shape.perimeter()}')
        print('-' * 50)
