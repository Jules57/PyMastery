"""
Вам дана строка.
Ваша задача - выяснить, содержит ли строка: буквенно-цифровые символы, алфавитные символы, цифры, строчные и
прописные символы.
Формат ввода
Одна строка, содержащая строку.

Формат вывода
В первой строке выведите True, если в ней есть алфавитно-цифровые символы. В противном случае выведите False.
Во второй строке выведите True, если в ней есть алфавитные символы. В противном случае выведите False.
В третьей строке выведите True, если есть цифры. В противном случае выведите False.
В четвертой строке выведите True, если в ней есть строчные символы. В противном случае выведите False.
В пятой строке выведите True, если есть прописные символы. В противном случае выведите False.
"""


def check_string(string: str) -> bool:
    print(string.isalnum())
    print(string.isalpha())
    print(string.isdigit())
    print(string.islower())
    print(string.isupper(), '\n')


check_string('12HELLO')
check_string('hello')
check_string('12345')
check_string('MYNAMEIS')
check_string('MY_NAME 123')
check_string('his name is 543')