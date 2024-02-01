"""
Задание 5
Дан список чисел. Поменяйте местами минимальный и максимальный элемент этого списка.

"""

numbers = [21, 34, 56, 11, 72, 36, 9, 53]

smallest = min(numbers)
biggest = max(numbers)

smallest_index = numbers.index(smallest)
biggest_index = numbers.index(biggest)

numbers[smallest_index] = biggest
numbers[biggest_index] = smallest

# numbers.remove(smallest_index)
# numbers.insert(smallest_index, biggest)
# numbers.remove(biggest_index)
# numbers.insert(biggest_index, smallest)

print(numbers)
