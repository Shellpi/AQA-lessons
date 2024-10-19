"""Hometask 04."""

import re

"""Variable that is given by default."""
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

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
""" Task 01 + code
Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')


""" Task 02 + code
Замініть .... на пробіл
"""

adwentures_of_tom_sawer = (adwentures_of_tom_sawer.replace('....', (' ')))


""" Task 03 + code
Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)


""" Task 04 + code
Виведіть, скількі разів у тексті зустрічається літера "h"
"""

adw_count_h_letter = adwentures_of_tom_sawer.count('h')
print(f"There are {adw_count_h_letter} 'h' letters in the text")


""" Task 05 + code
Виведіть, скільки слів у тексті починається з Великої літери?
"""

adw_text_split = adwentures_of_tom_sawer.split()
adw_capitalized_count = sum(1 for word in adw_text_split if word[0].isupper())
print(f'There are {adw_capitalized_count} capitalized words in the text.')


""" Task 06 + code
Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = adwentures_of_tom_sawer.find('Tom')
sec_index = adwentures_of_tom_sawer.find('Tom', first_index + 1)
print(f'Here is the index: {sec_index}')

""" Task 07 + code
Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')

""" Task 08 + code
Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adwentures_of_tom_sawer_sentences[3].lower())

""" Task 09 + code
Перевірте чи починається якесь речення з "By the time".
"""

sen_ch = any(
    sent.strip().startswith('By the time')
    for sent in adwentures_of_tom_sawer_sentences)
if sen_ch:
    print("There is a sentence that starts with 'By the time'.")
else:
    print("No sentence starts with 'By the time'.")


""" Task 10 and code
Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1]
split_last_sentence = last_sentence.split()
last_sentence_counter = len(split_last_sentence)
print(f'There are {last_sentence_counter} words in the last sentence.')
