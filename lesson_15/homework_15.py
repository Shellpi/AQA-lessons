"""Hometask 15."""

"""
Створіть клас геометричної фігури "Ромб".
Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при
заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus:
    """Rhombus class."""

    def __init__(self, angle_a, side_a):
        """Initialize the values."""
        self.angle_a = angle_a
        self.side_a = side_a

    def __setattr__(self, name, value):
        """Set attributes after they are checked."""
        if name == 'side_a':
            self._validate_side(value)
        elif name == 'angle_a':
            self._validate_angle(value)
            # Count the B angle value
            object.__setattr__(self, 'angle_b', round(180 - value, 2))
        object.__setattr__(self, name, value)

    @staticmethod
    def _validate_side(value):
        """Check the side value."""
        if not isinstance(value, (int, float)):
            raise TypeError('Incorrect value type.')
        if value <= 0:
            raise ValueError('The length should be higher than 0.')

    @staticmethod
    def _validate_angle(value):
        """Check the angle value."""
        if not isinstance(value, (int, float)):
            raise TypeError('Incorrect value type.')
        if not 0 < value < 180:
            raise ValueError('The angle value should be '
                             'higher than 0 and less than 180')

    def __str__(self):
        """Return the values."""
        return (
            f'Rhombus info:\n'
            f'The A side length: {self.side_a:.2f}\n'
            f'The A angle: {self.angle_a:.2f}\n'
            f'The B angle: {self.angle_b:.2f}\n'
            f"{'=' * 50}"
        )


rhombus1 = Rhombus(120.5628, 12)
print(rhombus1)
