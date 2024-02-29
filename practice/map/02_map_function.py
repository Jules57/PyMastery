"""
Напишите программу на Python для сложения трех заданных списков, используя Python map и лямбды.
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

final_list = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print(final_list)
