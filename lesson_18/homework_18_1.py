"""Hometask 18_1."""

"""
Генератори:
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('01'))


def gen_even_nums(limit):
    """Generate even numbers from 0 to limit."""
    if limit < 0:
        raise ValueError('Limit must be a non-negative number.')
    for i in range(limit):
        if i % 2 == 0:
            yield i


up_limit = 100
result = gen_even_nums(up_limit)
print(f'The even numbers from "0" to "{up_limit}":')
for number in result:
    print(number, end=' ')
print()


"""
Генератори:
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""

print(TASK_START_TEMPLATE.format('02'))


def gen_fibonacci(limit):
    """Fibonacci generator up to limit."""
    if limit < 0:
        raise ValueError('Limit must be a non-negative number.')
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


num = 100
sequence = gen_fibonacci(num)

print(f'Fibonacci sequence up to "{num}":')
for number in sequence:
    print(number, end=' ')
print()
