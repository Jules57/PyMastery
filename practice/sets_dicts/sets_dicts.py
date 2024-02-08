"""
Задание 1
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент
списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам задания ключей
в словарях.

Задание 2

Дана строка в виде случайной последовательности чисел от 0 до 9.

Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в
качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию
count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

Задание 3

Напишите программу, которая принимает сроку символов и вычисляет количество букв и цифр.
Входные данные:
Project Gutenberg offers over 59,000 free eBooks

Вывод:
LETTERS 36
DIGITS 5

Задание 4

Создайте словарь с данными о студентах: ключи - имена студентов, значения - баллы для каждого. Программа должна
определить средний балл и вывести имена студентов, чей балл выше среднего.

Задание 5

Напишите программу для подсчета количества символов (символьной частоты) во введенной строке.

Задание 6

Уникальные элементы из списка: Напишите функцию, которая принимает список и возвращает новый список только с
уникальными элементами из исходного списка, используя множества.

Задание 7

Пересечение множеств: Напишите функцию, которая принимает два списка и возвращает список, содержащий элементы,
которые присутствуют в обоих списках (пересечение множеств).

Задание 8

Объединение словарей: Напишите функцию, которая объединяет два словаря. Если ключ присутствует в обоих словарях,
соответствующие значения должны быть суммированы.

Задание 9

Частотный анализ: Напишите функцию, которая принимает строку и возвращает словарь, где ключами являются символы строки,
а значениями — частота их появления в строке.

Задание 10

Обратный словарь: Напишите функцию, которая инвертирует словарь, меняя местами ключи и значения. Если возникают
дубликаты значений, сохраните последний обработанный ключ.

Задание 11

Фильтрация по значению: Напишите функцию, которая принимает словарь и удаляет из него пары ключ-значение, где значение
не удовлетворяет заданному условию.

Задание 12

Разность множеств: Напишите функцию, которая принимает два списка и возвращает элементы, которые присутствуют в первом
списке, но отсутствуют во втором.

Задание 13

Симметричная разность множеств: Напишите функцию, которая принимает два списка и возвращает элементы, которые
уникальны для каждого списка (т.е. присутствуют только в одном из списков).

Задание 14

Группировка по значению: Напишите функцию, которая принимает список кортежей (ключ, значение) и группирует их в
словарь, где ключи — это уникальные ключи из кортежей, а значения — списки значений, соответствующих каждому ключу.

Задание 15

Сортировка словаря по значению: Напишите функцию, которая принимает словарь и возвращает список кортежей
(ключ, значение), отсортированный по значению от меньшего к большему.

Задание 16

Даны два словаря, в которых ключами являются строчные буквы латинского алфавита, а значениями - целые числа. В первом
словаре могут встречаться ключи или значения, которые присутствуют во втором словаре, или наоборот. Например,
содержимое словарей может быть следующим: a = {'x' : 1, 'y' : 2, 'z' : 3}, b = {'w' : 10, 'x' : 11, 'y' : 2}. Выведите
общие ключи для обоих словарей в одной строке через пробел.
"""
