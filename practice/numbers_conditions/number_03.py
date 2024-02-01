"""
Задание 1

Напишите программу, которая просит пользователя ввести количество секунд и работает следующим образом.
• В минуте 60 секунд. Если число введенных пользователем секунд больше или равно 60, то программа должна
преобразовать число секунд в минуты и секунды.
• В часе 3 600 секунд. Если число введенных пользователем секунд больше или равно 3 600, то программа должна
преобразовать число секунд в часы, минуты и секунды.
• В дне 86 400 секунд. Если число введенных пользователем секунд больше или равно 86 400, то программа должна
преобразовать число секунд в дни, часы, минуты и секунды."""

seconds = 240_020
# seconds = 45
# seconds = 10_000

if seconds >= 86400:
    days = seconds // 86400
    hours = seconds % 86400 // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds % 60
    print(f'You have {days} d. {hours} h. {minutes} min. {seconds} sec.')
elif seconds >= 3600:
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds % 60
    print(f'You have {hours} h. {minutes} min. {seconds} sec.')
elif seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60
    print(f'You have {minutes} min. {seconds} sec.')
else:
    print(f'You have {seconds} sec.')
