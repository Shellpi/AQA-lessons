"""Hometask 6_2."""

"""
Напишіть цикл, який буде вимагати від користувача ввести слово,
в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
"""

while True:
    word_input = input("Input your word with 'h':")
    if 'h' in word_input.lower():
        print("The 'h' is found")
        break
    else:
        print('Try again')
