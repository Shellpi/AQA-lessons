"""Hometask 6.1."""

"""
Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input()
"""

input_chars = input('Input your string:')
print(len(set(input_chars)) > 10)
