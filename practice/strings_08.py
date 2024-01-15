"""
Дано натуральное число. Найти число, которое получается в результате добавления 2 в начало и в конец входного числа.
"""

number = '19067'
new_number = '2' + number + '2'
# print(new_number)
print(f'{number:<10} {new_number:^50} END')
print(f'{number:<10} {new_number:>50} END')
print(f'{number:<10} {new_number:>50} END')
print(f'{new_number.ljust(50, "*")}')
print(f'{new_number.rjust(50, "*")}')
print(f'{new_number.center(50, "*")}')
