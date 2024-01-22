"""Пользователь задает переменную возраст. Если он старше 18 лет, выведите сообщение, что все хорошо, если нет, то
выведите сообщение, что не все хорошо.

Добавить к первому условию, если возраст больше чем 100, распечатать текст, что пользователь вводит нас
в заблуждение
(-...) 0-17    18-99  (>=100...)
Добавить вывод, является ли введенный возраст четным или нечетным.

Добавить, что пользователь вводит еще и имя. И если в имени есть буква 'a', то написать, что мы даже не собираемся его
проверять.

 <substring> / <element> in <str> / <list> / <tuple> / <set>

 Проверить если в имени есть буква 'v' или большая, или маленькая не важно. И возраст пользователя четный, то написать, что он
   выиграл приз, если нет, то не выиграл.
"""

age = 70
name = 'johnny'


if 'a' in name.lower():
    print("Not interested in further check.")
elif 18 > age > 0:
    print("You need to wait some time.")
elif 18 <= age < 100:
    print("Ok, you are adult and can dance with women.")
elif age >= 100:
    print("You are kidding me.")
else:
    print("Enter a valid value.")

if age % 2:
    print("Your age is odd.")
else:
    print("Your age is even.")

if 'v' in name.lower() and not age % 2:
    print("You are the winner")
else:
    print("You are not a winner today. Good luck!")
