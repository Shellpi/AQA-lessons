"""Hometask 7."""

""" Task 01.
Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити/доповнити.
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('01'))


def multiplication_table(number):
    """
    Функция выводит таблицу умножения для выбранного числа.

    Функция выводит таблицу умножения пока результат не превысит 25.
    """
    multiplier = 1  # Начинаем таблицу умножения с "1"
    while True:
        result = number * multiplier  # Наш результат
        if result > 25:  # Прерываем цикл если результат выдал больше 25
            break
        print(f'{number} x {multiplier} = {result}')
        multiplier += 1


# Пример использования
multiplication_table(3)


"""  Task 02.
Написати функцію, яка обчислює суму двох чисел.
"""

print(TASK_START_TEMPLATE.format('02'))


def two_digits_sum(a, b):
    """Функция суммирует 2 заданных числа."""
    return a + b


# Пример использования
print(two_digits_sum(18, 25))  # Результат: 43


"""  Task 03.
Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

print(TASK_START_TEMPLATE.format('03'))


def arithmetic_mean(num_list):
    """
    Функция для рассчета среднего арифметического из списка чисел.

    Функция обрабатывает список и фильтрует int и float значения.
    Функция суммирует полученные числовые значения и считает их кол-во.
    """
    numeric_values = [num for num in num_list if isinstance(num, (int, float))]
    if numeric_values:  # Проверка, что есть хотя бы одно число
        arith_mean = sum(numeric_values) / len(numeric_values)
        return (f'Среднее арифметическое: {arith_mean}')
    else:
        return 'Список не содержит числовых значений.'


# Пример использования
numbers = [10, 10.5, 10, 1999, 'a', 5.79]
print(arithmetic_mean(numbers))


"""  Task 04.
Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

print(TASK_START_TEMPLATE.format('04'))


def reversed_input(inp_us):
    """Функия принимает строку и возвращает ее в обдратном порядке."""
    return f"Ваша перевернутая строка: {inp_us[::-1]}"


# Пример использования
user_input = '123qwe qweasd !'
print(reversed_input(user_input))


"""  Task 05.
Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

print(TASK_START_TEMPLATE.format('05'))


def the_longest_word(words_list):
    """Функция для поиска самого длинного слова."""
    return (f'Самое длинное слово: '
            f'{max(words_list, key=len)}') if words_list else 'Список пуст.'


# Пример использования
user_input_list = ['apple', 'egg', 'qweqweqweqwe', 'testtest']
print(the_longest_word(user_input_list))


"""  Task 06.
Написати функцію, яка приймає два рядки та повертає індекс першого
входження другого рядка у перший рядок, якщо другий рядок є
підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print(TASK_START_TEMPLATE.format('06'))


def find_substring(str1, str2):
    """
    Функция принимает 2 строки и возвращает индекс 2ой строки в 1ой.

    При отсутствии 2ой строки в 1ой - выведет результат "-1".
    """
    index = str1.find(str2)
    return index


# Пример использования
str1 = 'Hello, world!'
str2 = 'world'
print(find_substring(str1, str2))  # поверне 7

# Пример использования 2
str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'cat'
print(find_substring(str1, str2))  # поверне -1


""" Task 07.
Написать функцию, которая рассчитает, сколько необходимо остановок
чтоб заправить полный бак чтоб доехать от точки А в точку Б.
Пользователь предоставляет длину пути, расход на 100 км и объем бака.
"""

print(TASK_START_TEMPLATE.format('07'))


def pit_stops_counter(length, consumption, tank_volume):
    """
    Функция для рассчета кол-ва остановок для преодоления всего пути.

    В функцию надо ввести 3 переменные (длина пути, потребление, объем бака).
    """
    petrol_need = length / 100 * consumption
    pit_stops = petrol_need // tank_volume
    if petrol_need % tank_volume == 0:
        return f'{int(pit_stops)} pit stops requires'
    else:
        return f'{int(pit_stops) + 1} pit stops requires'


# Пример использования
print(pit_stops_counter(1000, 100, 100))  # Результат: 10 pit stops requires

""" Task 08.
Есть список с числами, написать функцию,
которая посчитает сумму всех ПАРНЫХ чисел в этом списке.
Должны браться во внимание только INT значения. Пример взят из ДЗ 6.4.
"""

print(TASK_START_TEMPLATE.format('08'))


def paired_sum(*nums):
    """
    Функция, которая суммирует значения парных чисел из списка.

    Функция вычитывает только int значения.
    """
    even_int_sum = sum(num for num in nums
                       if isinstance(num, int) and num % 2 == 0)
    return f'Сумма парных чисел равна: {even_int_sum}'


# Пример использования
even_sum = paired_sum(10, 12, 1.2, 'qwerty', 13, 22, 15, 'testtest')
print(even_sum)  # Результат: Сумма парных чисел равна: 44


""" Task 09.
Написать функцию, которая будет считать кол-во букв/слов в тексте.
Считаются как прописные так и строчные.
Пользователь предоставляет текст и букву/слово. Текст взят из ДЗ 4.
"""

print(TASK_START_TEMPLATE.format('09'))


def string_counter(text, string):
    """Функция для подсчета выбранной буквы в тексте.

    Функция считает как прописные так и строчные буквы.
    """
    str_counter = text.lower().count(string.lower())
    return f'В тексте Ваша буква/слово встречается {str_counter} раз.'


# Пример использования
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the ....
shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had
traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(string_counter(adwentures_of_tom_sawer, 'iN'))  # Результат: 15


"""Task 10.
Напишите функцию, которая будет сортировать значения в словаре по
выбранному параметру. Функция должна выводить значения
как на увеличение, так и на уменьшение.
За основу взят словарь из домашнего задания 5 урока.
"""

print(TASK_START_TEMPLATE.format('10'))


def sort_car_data(data):
    """
    Функция для сортировки автомобильных данных в списках.

    Функция предлагает выбрать один из 5 вариантов.
    Функция предоставляет возможность сортировать список
    по возрастанию и убыванию (пользователь делает выбор).
    На каждом этапе выбора идет обработка на неправильный ответ.
    """
    while True:
        print('Пожалуйста, выберите параметр сортировки: ')
        print('0: Цвет, 1: Год, 2: Объем двигателя, 3: Тип кузова, 4: Цена')

        try:  # Обрабатываем корректность ввода
            index = int(input('Введите цифру с параметром (от 0 до 4): '))
            if index not in range(5):
                print('Пожалуйста, введите цифру от 0 до 4.')
                continue
        except ValueError:  # При некорректном вводе выводим сообщение
            print('Введите корректное число с индексом.')
            continue

        print('Вам отсортировать список по возрастанию или убыванию: ')
        print('0: По возрастанию, 1: По убыванию')

        try:  # Обрабатываем корректность ввода
            order = int(input('Введите цифру с параметром (от 0 до 1): '))
            if order not in (0, 1):
                print('Пожалуйста, введите цифру 0 или 1.')
                continue
            reverse = order == 1  # При 1 у нас reverse=True
        except ValueError:  # При некорректном вводе выводим сообщение
            print('Введите корректное число.')
            continue

        # Сортируем данные из словаря по выбранным пользователем параметрам
        sorted_data = dict(sorted(
            data.items(), key=lambda item: item[1][index], reverse=reverse))
        return sorted_data


# Пример использования

car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000),
}
sorted_cars = sort_car_data(car_data)
print(sorted_cars)
