"""
Игра "Камень, ножницы, бумага". Напишите программу, которая дает пользователю возможность поиграть с компьютером в
игру "Камень, ножницы, бумага". Программа должна работать следующим образом.

Когда программа запускается, генерируется случайное число в диапазоне от 1 до 3. Если число равняется 1, то компьютер
выбрал камень. Если число равняется 2, то компьютер выбрал ножницы. Если число равняется 3, то компьютер выбрал бумагу.
(Пока не показывайте выбор компьютера.)

Пользователь вводит на клавиатуре выбранный вариант "stone", "scissors" или "paper".

Выбор компьютера выводится на экран.

Победитель выбирается согласно следующим правилам:

- если один игрок выбирает камень, а другой игрок выбирает ножницы, то побеждает камень (камень разбивает ножницы);
- если один игрок выбирает ножницы, а другой игрок выбирает бумагу, то побеждают ножницы (ножницы режут бумагу);
- если один игрок выбирает бумагу, а другой игрок выбирает камень, то побеждает бумага (бумага заворачивает камень);
- если оба игрока делают одинаковый выбор, то для определения победителя нужно сыграть повторный раунд.
"""

import random

CHOICES = {1: 'stone', 2: 'scissors', 3: 'paper'}


def get_computer_choice():
    comp_choice = random.randint(1, 3)
    return comp_choice


def get_user_choice():
    user_choice = int(input('Make your turn (1 for stone, 2 for scissors, 3 for paper): '))
    if user_choice in CHOICES:
        return user_choice


def define_winner(comp_choice, user_choice):
    if comp_choice == user_choice:
        print('Draw! Try again!')
    elif (comp_choice == 1 and user_choice == 2) or \
            (comp_choice == 2 and user_choice == 3) or \
            (comp_choice == 3 and user_choice == 1):
        print('Sorry! You are not lucky this time :(')
    else:
        print('Congratulations! You won!')


def main():
    keep_going = 'y'

    print(f'Hello and welcome to our magnificent game! \n'
          f'In this game you can choose one of three options: stone (1), scissors (2) and paper (3). \n'
          f'To stop playing enter "Exit"')

    while keep_going != 'exit':
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(f'Computer chose: {CHOICES[computer_choice]}')
        define_winner(computer_choice, user_choice)
        keep_going = input('To continue press "y", to exit enter "Exit"').lower()


main()
