"""
Напишите программу на Python для возведения элементов списка в квадрат с помощью функции map().
"""

my_list = [1, 4, 27, 2, 31, 46, 82, 16]

squared = list(map(lambda x: x ** 2, my_list))

print(squared)
