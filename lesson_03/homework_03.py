"""The 3rd lection hometask."""

"""Task 1 + code
alice_in_wonderland = '"Would you tell me,
please, which way I ought to go from here?"\n"
That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так,
            щоб вона займала декілька фізичних лінії """

alice_in_wonderland = ('"Would you tell me, please, which '
                       'way I ought to go from here?"\n'
                       '"That depends a good deal on '
                       'where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter '
                       'which way you go," said the Cat.\n'
                       '—— so long as I get somewhere," '
                       'Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," '
                       'said the Cat, "if you only walk long enough."')

print(alice_in_wonderland)


""" Task 2 + code
# task02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті"""

alice_in_wonderland = ('"Would you tell me, please, '
                       'which way I ought to go from here?"\n'
                       '"That depends a good deal on '
                       'where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" '
                       'said Alice.\n'
                       '"Then it doesn\'t matter which '
                       'way you go," said the Cat.\n'
                       '—— so long as I get somewhere," '
                       'Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," '
                       'said the Cat, "if you only walk long enough."')
print(f' Single quotes num: {alice_in_wonderland.count("'")}')


""" Task 3 + code
# task 03 == Виведіть змінну alice_in_wonderland на друк """


alice_in_wonderland = ('"Would you tell me, please, which way I '
                       'ought to go from here?"\n'
                       '"That depends a good deal on where you '
                       'want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," '
                       'said the Cat.\n'
                       '—— so long as I get somewhere," '
                       'Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, '
                       '"if you only walk long enough."')

print(alice_in_wonderland)


""" Tasks 4-10 description
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

"""
Task 4 + code
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_square = 436402
azov_sea_square = 37800
two_seas_square = black_sea_square + azov_sea_square
print('The total square for Azov and Black seas is:', two_seas_square)

"""
Task 5 + code
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
fir_and_sec_w = 250449
sec_and_thi_w = 222950
sec_war = fir_and_sec_w + sec_and_thi_w - total_goods
fir_war = fir_and_sec_w - sec_war
thi_war = sec_and_thi_w - sec_war
print('The first warehouse has:', fir_war, 'goods\n'
      'The second warehouse has:', sec_war, 'goods\n'
      'The third warehouse has:', thi_war, 'goods')

"""
Task 6 + code
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

price_per_month = 1179
months = 18
total_value = price_per_month * months
print('The total PC price is:', total_value)


"""
Task 7 + code
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""


print(f' a) Answer: {8019 % 8} ')
print(f' b) Answer: {9907 % 9} ')
print(f' c) Answer: {2789 % 5} ')
print(f' d) Answer: {7248 % 6} ')
print(f' e) Answer: {7128 % 5} ')
print(f' f) Answer: {19224 % 9} ')

"""# For cases if you want to test your own input values
# x = int(input('Input your value: '))
# y = int(input('Input the number you want to divide by: '))
# z = x % y
# print('The remainder is: ',z) """


"""
Task 8 + code
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

piz_big_count = 4
piz_big_price = 274
piz_m_count = 2
piz_m_price = 218
juice_count = 4
juice_price = 35
cake_count = 1
cake_price = 350
water_count = 3
water_price = 21
tot_piz_price = (piz_m_price * piz_m_count) + (piz_big_count * piz_big_price)
tot_jui_price = (juice_price * juice_count)
tot_cake_price = (cake_price * cake_count)
tot_water_price = (water_price * water_count)
total = (tot_piz_price + tot_jui_price + tot_water_price + tot_cake_price)
print('Total price is: ', total)


"""
Task 9 + code
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos_count = 232
maximum_page_photo = 8
pages_for_all_photos = total_photos_count // maximum_page_photo
if total_photos_count % maximum_page_photo == 0:
    print('Igor needs', pages_for_all_photos, 'pages')
else:
    print('Igor needs', pages_for_all_photos + 1, 'pages')


"""
Task 10 + code
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

full_path = 1600
petrol_per_100km = 9
tank_capacity = 48
petrol_need = full_path / 100 * petrol_per_100km
print('Petrol is needed for the full path: ', petrol_need)
pit_stops = petrol_need // tank_capacity
if petrol_need % tank_capacity == 0:
    print(int(pit_stops), 'pit stops requires')
else:
    print(int(pit_stops + 1), 'pit stops requires')
