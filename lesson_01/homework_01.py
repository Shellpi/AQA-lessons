"""The first lecture hometask."""

"""
Hometask 1 + fix.

# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
    print("world!")
"""

print('Hello', end=' ')
print('world!')


"""
Hometask 2 + fix.

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
print(f"{hello} {world}!")
"""

hello = 'Hello'
world = 'world'
if True:
    print(hello, world)


"""
Hometask 3 + fix.

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print()
"""

for letter in 'Hello world!':
    print(letter)

"""
Hometask 4 + fix.

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = x
"""

apples = 2
bananas = apples * 4


"""
Hometask 5 + fix.

# task 05 == виправте назви змінних
1_storona = 1
?torona_2 = 2
сторона_3 = 3
$torona_4 = 4
"""

storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

"""
Hometask 6 + fix.

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = ? + ? + ? + ?
print()
"""

perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)

"""
Description what to do for 7-10 tasks.
    # Задачі 07 - 10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

"""
Hometask 7.

У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print('Total trees:', total_trees)


"""
Hometask 8.

До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

morning_t = 5
afternoon_t = morning_t - 10
evening_t = afternoon_t + 4
print('Evening temperature is:', evening_t)


"""
Hometask 9.

Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys = 24
girls = boys // 2
boys_today = boys - 1
girls_today = girls - 2
present_today = boys_today + girls_today
print(present_today, 'kids are present today')


"""
Hometask 10.

Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
total = (book_1 + book_2 + book_3) * 1
print('It will cost', total)
