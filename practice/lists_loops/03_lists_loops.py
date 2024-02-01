"""
Задание 3
Пользователь вводит числа до тех пор, пока не введет слово ‘No’. Поместите введенные числа в список. Подсчитайте
количество четных и нечетных элементов в списке.
"""

value = input('Enter a positive integer number from 1 to 1000000: ')
numbers = []

while value.lower() != 'no':
    if value.isdigit():
        numbers.append(int(value))
        value = input('Number: ')
    else:
        value = input('Please, enter a valid number: ')

# Выборка четных элементов в цикле
# even_numbers = []
# for elem in numbers:
#     if not elem % 2:
#         even_numbers.append(elem)

# Выборка четных элементов list comprehension
# even_numbers = len([elem for elem in numbers if not elem % 2])

# Подсчет количества четных и нечетных элементов в списках
# even_count = len(even_numbers)
# odd_count = len(numbers) - even_numbers


odd_count = 0
even_count = 0

for elem in numbers:
    if elem % 2:
        odd_count += 1
    else:
        even_count += 1

print(f'The number of even numbers is {even_count}\n'
      f'The number of odd numbers is {odd_count}')
