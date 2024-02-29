"""
Напишите программу на Python для преобразования всех символов в прописные и строчные и удаления дублирующихся букв из
заданной последовательности. Используйте функцию map().
"""

chars = ['a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a']
# output
# ('a', 'A'), ('b', 'B', ...)

transformed_chars = set(map(lambda ch: (ch.lower(), ch.upper()), chars))

print(transformed_chars)
