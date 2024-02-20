"""
Дана строка в виде случайной последовательности чисел от 0 до 9.

Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в
качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию
count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

count_dict = {0: 5, 1: 6, 2: 3, ...}
1. Создать строку чисел - '000001111123456784635298652351'
2. Создать словарь
3. Преобразовать строку в множество
4. Посчитать числа в строке
5. Найти 3 самых часто встречающихся числа
"""


def count_it(number_string: str) -> dict:
    # number_dict = {int(elem): number_string.count(elem) for elem in set(number_string)}

    number_dict = {}
    seq = set(number_string)
    for elem in seq:
        number_dict[int(elem)] = number_string.count(elem)
    sorted_dict = dict(sorted(number_dict.items(), key=lambda x: x[1], reverse=True)[:3])
    return sorted_dict


string = '000001111123456784635298652351'
final_dict = count_it(string)
print(final_dict)
