"""
Даны два словаря, в которых ключами являются строчные буквы латинского алфавита, а значениями - целые числа. В первом
словаре могут встречаться ключи, которые присутствуют во втором словаре, или наоборот. Например,
содержимое словарей может быть следующим: a = {'x' : 1, 'y' : 2, 'z' : 3}, b = {'w' : 10, 'x' : 11, 'y' : 2}. Выведите
общие ключи для обоих словарей в одной строке через пробел.
"""

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# Dicts intersection
# common_keys = a.keys() & b.keys()
# print(' '.join(common_keys))

# Solution with list comprehension
# common_keys = ' '.join([key for key in a.keys() if key in b.keys()])
# print(common_keys)

# Traditional solution with a for loop
common_keys = []
for key in a.keys():
    if key in b.keys():
        common_keys.append(key)

print(' '.join(common_keys))
