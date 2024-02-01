"""
Дана строка. Замените регистр символов в ней так, чтобы первая буква каждого слова была в верхнем регистре, а
остальные буквы - в нижнем регистре.

Ввод:
<= A scandal in Bohemia
=> A Scandal In Bohemia

<= The adventure of the Blue Carbuncle
=> The Adventure Of The Blue Carbuncle

<= The Boscombe valley mystery
=> The Boscombe Valley Mystery
"""

string = 'The Boscombe valley mystery'
print(string.title())
