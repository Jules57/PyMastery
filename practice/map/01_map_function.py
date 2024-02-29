"""
Напишите программу на Python, которая утроит все числа в заданном списке целых чисел. Используйте map Python.
"""


# triple_it = lambda num: num * 3

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 42]

triple_list = list(map(lambda num: num * 3, my_list))

print(triple_list)
