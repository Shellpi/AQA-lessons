"""Hometask 8."""

"""
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою.
Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову
функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі),
вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try/except, щоб уникнути інших символів,
окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('01'))


def sum_numbers_in_string(s):
    """
    Calculate the sum of integer values separated by commas in a string.

    If any non-integer value is encountered,
    it returns the message "Не можу це зробити!"
    """
    try:
        return sum(int(num) for num in s.split(','))
    except ValueError:
        return 'Не можу це зробити!'


# Test data
data = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
data2 = []

# Output the sum for each element in the list
for item in data:
    result = data2.append(sum_numbers_in_string(item))

print(data2)
