"""
Задание 6

Дано число из 3 цифр. Определить сумму первой и последней цифр и сравнить ее со значением второго числа. Вывести
сообщение о результате сравнения.
"""

number = 8573

zero = number // 1000
first = number % 1000 // 100
second = number % 100 // 10
third = number % 10

if zero + third == second + first:
    print('Success')
else:
    print('Failure')
