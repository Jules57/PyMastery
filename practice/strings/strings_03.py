"""
Прочитайте заданную строку, измените символ в заданном индексе, а затем выведите измененную строку.
Описание функции
Напишите функцию mutate_string в редакторе ниже.
mutate_string имеет следующие параметры:
str string: строка для изменения
int position: индекс, по которому нужно вставить символ
str character: символ для вставки

Возвращает
str: измененная строка
'hahabubu' 5 'k' 'hahabkbu'
'apple' + 'pie' = 'apple pie'

Псевдокод:
1. Создать пустую переменную для новой строки

3. Получить первую часть строки от начала до position   => string[:position]
4. Конкатенировать первую часть и character             => string[:position] + character
5. Конкатенировать вторую часть от position до конца    => string[:position] + character + string[position:]

"""


def mutate_string(string: str, position: int, character: str) -> str:
    # new_string = ''
    first_part = string[:position]
    # new_string += first_part
    # next_char = character
    # new_string += next_char
    last_part = string[position + 1:]
    # new_string += last_part

    new_string = first_part + character + last_part
    print(new_string)

    print(string[:position] + character + string[position + 1:])
    print(string.replace(string[position], character, 1))

    return f'{string[:position]}{character}{string[position + 1:]}'


# string = input('Enter your string: ')
# position = int(input('Enter the position of the symbol to change: '))
# character = input(' Enter the character to change: ')

mutate_string('hahabubu', 5, character='K')
