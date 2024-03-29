"""
Уникальные элементы из списка: Напишите функцию, которая принимает список и возвращает новый список только с
уникальными элементами из исходного списка, используя множества.

Пересечение множеств: Напишите функцию, которая принимает два списка и возвращает список, содержащий элементы,
которые присутствуют в обоих списках (пересечение множеств).
1. Создать список 1
2. Создать список 2
3. Преобразовать список 1 в множество 1
4. Преобразовать список 2 в множество 2
5. Найти общие элементы в обоих множествах
6. Преобразовать в список

"""


def make_unique(mylist: list) -> list:
    return list(set(mylist))


def find_common(mylist1: list, mylist2: list) -> list:
    set1 = set(mylist1)
    set2 = set(mylist2)
    common = list(set1.intersection(set2))
    return common


numbers = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 19]
numbers2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 19, 50]

print(make_unique(numbers))
print(find_common(numbers, numbers2))
