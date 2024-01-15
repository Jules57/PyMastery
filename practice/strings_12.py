"""
Дано два слова. Составить программу, которая определяет, начинается ли первое слово на ту же букву, на которую
заканчивается второе.
"""

phrase = 'mary adam'

if phrase[0] == phrase[-1]:
    print(True)
else:
    print(False)

print(f'{phrase.startswith(phrase[0]) == phrase.endswith(phrase[0])}')
print(f'{phrase.startswith(phrase[-1]) == phrase.endswith(phrase[-1])}')
