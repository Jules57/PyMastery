"""
Симметричная разность множеств: Напишите функцию, которая принимает два списка и возвращает элементы, которые
уникальны для каждого списка (т.е. присутствуют только в одном из списков).
"""


def find_symmetric_difference(lst1: list, lst2: list) -> list:
    return list(set(lst1).symmetric_difference(set(lst2)))


my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [3, 4, 5, 6, 12, 13, 14, 15, 16, 17, 18, 19]

print(find_symmetric_difference(my_list1, my_list2))

# print(find_symmetric_difference([1, 2, 3, 4, 5, 6, 7, 8, 9],
#                                 [3, 4, 5, 6, 12, 13, 14, 15, 16, 17, 18, 19]))
