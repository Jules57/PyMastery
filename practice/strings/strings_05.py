"""
Напишите программу, которая принимает у пользователя строку и выводит эту строку в верхнем и нижнем регистре.
"""


def transform_string(string: str) -> str:
    return f'{string.upper()}, {string.lower()}'


print(transform_string('HELLO, WORLD'))
print(transform_string('hello, world'))
