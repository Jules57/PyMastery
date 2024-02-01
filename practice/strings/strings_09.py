"""
Пользователь вводит строку и набор символов. Напишите программу, которая проверяет, начинается ли строка с
указанных символов.
"""
string = 'Mary went to the forest to find some cranberries'
character_set = 'Mary went to the forest'
end_part = 'cranberries'

print(string.startswith(character_set))
print(string.endswith(end_part))
