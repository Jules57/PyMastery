"""
Частотный анализ: Напишите функцию, которая принимает строку и возвращает словарь, где ключами являются символы строки,
а значениями — частота их появления в строке.

1. Получить строку
2. Получить из строки множество
3. Пройти по всем элементам множества
4. Считаем количество вхождений каждого элемента (метод count())
5. Кладем в словарь символ (ключ) и количество его повторений в строке (значение)
6. Отдаем словарь
"""

string = 'aaaaaaa bbbbb ccccc ddd eee ffff llllllllllllll'

# unique_chars = set(string)
# char_count = {}
#
# for char in unique_chars:
#     char_count[char] = string.count(char)


char_count = {char: string.count(char) for char in set(string)}
print(char_count)
