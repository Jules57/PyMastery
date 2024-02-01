"""
Дано две строки, которые могут содержать пробелы. Выведите слово Yes, если первая строка является подстрокой второй
строки, и No в противном случае
"""

first = 'word'
second = 'some other word'

if second.find(first) != -1:
    print('YES')
else:
    print('NO')

print('YES') if second.find(first) != -1 else print('NO')
# (statement for True) if <condition> else (statement for False)
