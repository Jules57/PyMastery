"""
Задание 2

Дата 10 июня 1960 года является особенной, потому что если ее записать в приведенном ниже формате, то произведение дня
и месяца равняется году:
10.06.60
Разработайте программу, которая просит пользователя ввести месяц (в числовой форме), день и двузначный год. Затем
программа должна определить, равняется ли произведение дня и месяца году. Если это так, то она должна вывести сообщение,
 говорящее, что введенная дата является магической. В противном случае она должна вывести сообщение, что дата не
 является магической.
"""

day = 10
month = 2
year = 20

# day = int(input('Day: '))
# month = int(input('Month: '))
# year = int(input('Year: '))

if day * month == year:
    print("Congratulations!")
else:
    print("The date is not a magic one.")