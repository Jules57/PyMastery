"""
Задание 5

Дано однобайтовое десятичное число (от 128 до 255). Проверьте, является ли двоичное представление десятичного числа
палиндромом, с учетом сохранения старших нулей в двоичном представлении.
Пример таких двоичных чисел: 102 - 01100110, 129 - 10000001

Input: 231, 255, 178
Output: True, True, False

128    2**7
64     2**6
32     2**5
16     2**4
8      2**3
4      2**2
2      2**1
1      2**0

Псевдокод:
1. Привести число в двоичное представление путем деления на степени двойки
2. Проверить на палиндромность
"""

number = 178
# 11100111

binary_string = ''

for i in range(7, -1, -1):
    if number >= 2**i:
        number -= 2**i
        binary_string += '1'
    else:
        binary_string += '0'

print(f'{binary_string[::-1] == binary_string}')
