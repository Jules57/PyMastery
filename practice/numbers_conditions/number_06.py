"""
Задание 6

Дано число из 3 цифр. Определить, равен ли квадрат суммы его цифр сумме кубов его цифр.

Input: 123, 210, 150
Output: True, True, False
"""

number = 150

first = number // 100
second = number % 100 // 10
third = number % 10

if (first + second + third) ** 2 == first ** 3 + second ** 3 + third ** 3:
    print('True')
else:
    print('False')
