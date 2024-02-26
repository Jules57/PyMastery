"""
Какова стоимость страховки? Многие финансовые эксперты рекомендуют собственникам недвижимого имущества страховать
свои дома или постройки как минимум на 80% суммы замещения строения. Напишите программу, которая просит пользователя
ввести стоимость строения и затем показывает минимальную страховую сумму, на которую он должен застраховать
недвижимое имущество.
"""

MIN_RATE = .8


def calculate_insurance_amount(building_price: float) -> float:
    return building_price * MIN_RATE


amount = float(input('Enter the cost of your building: '))
print(f'The insurance amount is ${calculate_insurance_amount(amount):.2f}.')
