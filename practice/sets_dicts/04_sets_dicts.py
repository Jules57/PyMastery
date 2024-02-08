""""
Напишите программу, которая принимает сроку символов и вычисляет количество букв и цифр.
Входные данные:
Project Gutenberg offers over 59,000 free eBooks

Вывод:
LETTERS 36
DIGITS 5
"""

count = {'letters': 0, 'digits': 0}
string = 'Project Gutenberg offers over 59,000 free eBooks'

for char in string:
    if char.isalpha():
        count['letters'] += 1
    elif char.isdigit():
        count['digits'] += 1

print(count)
