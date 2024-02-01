"""
Пользователь вводит два имени. Используя условия, программа должна вывести имена в алфавитном порядке.
Input:
Name 1: Guido van Rossum
Name 2: Dennis Ritchie

Output:
Dennis Ritchie
Guido van Rossum
"""

name1 = 'Dennis Ritchie'
name2 = 'Guido van Rossum'

if ord(name1.lower()[0]) <= ord(name2.lower()[0]):
    print(f'{name1}\n'
          f'{name2}')
else:
    print(f'{name2}\n'
          f'{name1}')

if name1.lower()[0] >= name2.lower()[0]:
    print(f'{name2}\n'
          f'{name1}')
else:
    print(f'{name1}\n'
          f'{name2}')
