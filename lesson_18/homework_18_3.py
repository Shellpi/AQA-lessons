"""Hometask 18_3."""

"""
Декоратори:
Напишіть декоратор, який логує аргументи та результати викликаної функції.
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('05'))


def deco(func):
    """Log arg/kwargs and the function result."""

    def wrapper(*args, **kwargs):
        print(f'The function name: {func.__name__}')
        print(f'Arguments used: args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        return result
    return wrapper


@deco
def add(a, b):
    """Summ 2 elements."""
    return a + b


@deco
def greet(name, greeting='Hello'):
    """Return greetings."""
    return f'{greeting}, {name}!'


print(add(151, 5))
print('-' * 50)
print(greet('Vlad', greeting='Hi'))


"""
Декоратори:
Створіть декоратор, який перехоплює та обробляє винятки,
які виникають в ході виконання функції.
"""


print(TASK_START_TEMPLATE.format('06'))


def exception_handler(func):
    """Catch and log exceptions that occur during function execution."""
    def wrapper2(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            return f"An error occurred in function '{func.__name__}': {exc}"
    return wrapper2


@exception_handler
def divide(a, b):
    """Divide 2 elements."""
    return a / b


print(divide(10, 2))
print(divide(10, 0))
