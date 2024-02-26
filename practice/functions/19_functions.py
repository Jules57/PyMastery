"""
Игра в угадывание случайного числа. Напишите программу, которая генерирует случайное число в диапазоне от 1 до 100 и
просит пользователя угадать это число. Если догадка пользователя больше случайного числа, то программа должна
вывести сообщение "Слишком много, попробуйте еще раз". Если догадка меньше случайного числа, то программа должна
вывести сообщение "Слишком мало, попробуйте еще раз". Если пользователь число угадывает, то приложение должно
поздравить пользователя и сгенерировать новое случайное число, чтобы возобновить игру.
Необязательное улучшение: улучшите игру, чтобы она вела подсчет попыток угадать, которые делает пользователь. Когда
пользователь угадывает случайное число правильно, программа должна показать количество попыток.
"""

import random


def validate_guess(choice, secret):
    if choice > secret:
        print('Too much!')
    elif choice < secret:
        print('Too little')


keep_going = 'yes'

while keep_going == 'yes':
    secret_number = random.randint(1, 1000)
    print('I am thinking of a number between 1 and 1000.')
    guess = int(input("Your best guess: "))
    counter = 0

    while guess != secret_number:
        validate_guess(guess, secret_number)
        guess = int(input("Your best guess: "))
        counter += 1

    print('Great job! You got it!')
    print(f'Tries: {counter}')
    keep_going = input('Shall we continue? ("Yes" or "No") ').lower()

print('Thanks for playing!')
