"""
Напишите программу на Python, чтобы перечислить список заданных строк по отдельности с помощью Python map.
"""

my_string = ['aaaa', 'bbbb', 'cccc', 'dddd']

list_string = list(map(list, my_string))
print(list_string)
# [['a', 'a', 'a', 'a'], ['b', 'b', 'b', 'b'], ['c', 'c', 'c', 'c'], ['d', 'd', 'd', 'd']]
