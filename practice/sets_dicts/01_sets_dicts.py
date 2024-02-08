"""
Объединение словарей: Напишите функцию, которая объединяет два словаря. Если ключ присутствует в обоих словарях,
соответствующие значения должны быть суммированы.

1. Создать словарь 1
2. Создать словарь 2
3. Создать пустой словарь
4. Собрать все ключи в переменную keys
5. Обойти все ключи и проверить условие их наличия в одном или обоих словарях
6. Если ключ есть только в одном словаре, то добавить в новый словарь этот ключ и его значение
7. Если ключ есть в обоих словарях, то добавить в новый словарь этот ключ и сумму его значений из обоих словарей
8. Вернуть итоговый словарь
"""

fruits = {'apple': 1, 'banana': 2, 'cherry': 3, 'kiwi': 4, 'pineapple': 5}
bad_fruits = {'cherry': 13, 'kiwi': 40, 'pineapple': 19, 'orange': 7, 'melon': 10}
keys = set(list(fruits.keys()) + list(bad_fruits.keys()))

good_fruits = {}

for key in keys:
    if key in fruits and key in bad_fruits:
        good_fruits[key] = fruits[key] + bad_fruits[key]
    elif key in fruits:
        good_fruits[key] = fruits[key]
    else:
        good_fruits[key] = bad_fruits[key]

print(good_fruits)
