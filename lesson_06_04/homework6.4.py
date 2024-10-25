"""Hometask 6.4."""

"""
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""

numbers = list(map(int, input('Enter numbers separated by spaces : ').split()))
even_sum = sum(num for num in numbers if num % 2 == 0)
print('The sum of even numbers: ', even_sum)
