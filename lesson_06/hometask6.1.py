"""Hometask 6.1."""

"""
Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input()
"""

input_chars = input('Input your string:')
unique_chars = set(input_chars)
if len(unique_chars) > 10:
    print(True)
else:
    print(False)
