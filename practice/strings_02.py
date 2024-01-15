"""
Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются
слева направо и справа налево. Подсказка. Используйте срезы."""

potential_palindrome = 'Sir I demand I am a maid named Iris'

print(potential_palindrome.lower().replace(' ', '') ==
      potential_palindrome.lower().replace(' ', '')[::-1])
