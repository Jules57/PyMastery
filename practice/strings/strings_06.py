"""
Напишите программу, которая выводит на экран строку из 5 копий последних двух символов введенной пользователем строки
(длина введенной строки должна быть не меньше 2 символов)
"""

string = input('Enter your string: ')
print((string[-2:] + ' ') * 5)
print(string[-4:] + ' ' * 3)