"""Hometask 16_1."""

import pytest

"""
Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department,
а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager,
так і від Developer. Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
а також атрибут team_size, який вказує на кількість
розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager
та Developer у класі TeamLead.
"""


class Employee(object):
    """Base Employee class."""

    def __init__(self, name, salary, **kwargs):
        """Initialize Employee with name and salary."""
        self.name = name
        self.salary = salary


class Manager(Employee):
    """Manager class inheriting from Employee."""

    def __init__(self, name, salary, department, **kwargs):
        """Initialize Manager attributes."""
        super().__init__(name, salary, **kwargs)
        self.department = department


class Developer(Employee):
    """Developer class inheriting from Employee."""

    def __init__(self, name, salary, programming_language, **kwargs):
        """Initialize Developer attributes."""
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    """TeamLead class inheriting from Manager and Developer."""

    def __init__(self, name, salary, department, team_size,
                 programming_language):
        """Initialize TeanLead attributes."""
        super().__init__(name, salary, department,
                         programming_language=programming_language)
        self.team_size = team_size


# Test fixtures and cases
@pytest.fixture
def team_lead():
    """Test data."""
    return TeamLead('Vlad', 10000, 'IT', 10, 'Python')


def test_team_lead_attributes(team_lead):
    """Test TeamLead class attributes."""
    assert team_lead.name == 'Vlad'
    assert team_lead.salary == 10000
    assert team_lead.department == 'IT'
    assert team_lead.programming_language == 'Python'
    assert team_lead.team_size == 10
