"""
Задание 1
Пользователь вводит числа a и b. Создать список, содержащий квадраты целых четных чисел, расположенных между ними.

"""

first = 3
second = 15

squares = []
for i in range(first, second):
    if not i % 2:
        squares.append(i**2)

print(squares)

squares = [i**2 for i in range(first, second) if not i % 2]
print(squares)

# list comprehension
# variable = [final_element for_expression if <condition>]
