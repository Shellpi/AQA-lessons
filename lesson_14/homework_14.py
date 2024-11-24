"""Hometask 14."""

"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище",
"вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати
середній бал студента. Виведіть інформацію про студента та
змініть його середній бал.
"""


class Student:
    """Add student and modify his average grade."""

    def __init__(self, name: str, surname: str, age: int, av_points: float):
        """Initialize student's info."""
        self.name = name
        self.surname = surname
        self.age = age
        self.av_points = av_points
        print(f'New student is added: \nName: {name}, surname: {surname}, '
              f'age: {age}, average_points: {av_points}'
              f'\n {"=" * 50}')

    def update_av_points(self, new_grade: float):
        """Update student av_points."""
        self.av_points = new_grade
        print(f'New grade is set: \nName: {self.name}, '
              f'surname: {self.surname}, '
              f'age: {self.age}, average_points: {new_grade}'
              f'\n {"=" * 50}')

    def __str__(self):
        """Return the student info."""
        return (f'Student Info:\n'
                f'Name: {self.name}\n'
                f'Surname: {self.surname}\n'
                f'Age: {self.age}\n'
                f'Average Points: {self.av_points}\n'
                f'{"=" * 50}')


student1 = Student('Vlad', 'Putintsev', 32, 45)
student1.update_av_points(85)
print(student1)
