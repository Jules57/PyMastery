"""
Задание 2
Пользователь вводит числа до тех пор, пока не введет слово 'No'. Поместите введенные числа в список. Выведите на экран
только нечетные элементы списка.
"""

value = input('Enter a positive integer number from 1 to 1000000: ')
numbers = []

while value.lower() != 'no':
    if value.isdigit():
        numbers.append(int(value))
        value = input('Number: ')
    else:
        value = input('Please, enter a valid number: ')

# Цикл с использованием range()
# odd_elements = []
# for i in range(len(numbers)):
#     if numbers[i] % 2:
#         odd_elements.append(numbers[i])


# Цикл обхода элементов
# odd_elements = []
# for elem in numbers:
#     if elem % 2:
#         odd_elements.append(elem)

odd_elements = [elem for elem in numbers if elem % 2]

print(odd_elements)



# Остаток от деления для четных чисел дает 0, для нечетных дает 1
# 0 преобразуется в False
# 1 преобразуется в True
# Следовательно, если нам нужны только нечетные элементы, то достаточно записи if element % 2 (который возвращает 1)
# 1 преобразуется в True, и мы выполняет блок if
