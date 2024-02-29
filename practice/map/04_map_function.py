"""
Напишите программу на Python для создания списка, содержащего степень указанного числа в базисе, возведенную в степень
соответствующего числа в индексе, используя Python map.

Write a Python program to create a list containing the power of said number in bases raised to the corresponding number
in the index using Python map.
"""

bases = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

powered_nums = list(map(pow, numbers, bases))

print(powered_nums)
# [1, 4, 27, 256, 3125, 46656, 823543, 16777216]
