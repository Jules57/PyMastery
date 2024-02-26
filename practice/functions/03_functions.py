"""
Расходы на автомобиль. Напишите программу, которая просит пользователя ввести месячные расходы на следующие нужды,
связанные с его автомобилем: платеж по кредиту, страховка, бензин, машинное масло, шины и техобслуживание. Затем
программа должна показать общую месячную стоимость и общую годовую стоимость этих расходов.
"""

MONTHS_IN_YEAR = 12


def get_monthly_cost(*args):
    return sum(args)


def get_yearly_cost(cost):
    return cost * MONTHS_IN_YEAR


credit_payment = float(input('Enter your monthly credit payment: '))
insurance_payment = float(input('Enter your insurance payment: '))
fuel = float(input('Enter your fuel costs: '))
tyres = float(input('Enter your tyres costs: '))
maintenance = float(input('Enter your maintenance cost: '))

monthly_cost = get_monthly_cost(credit_payment, insurance_payment, fuel, tyres, maintenance)
yearly_cost = get_yearly_cost(monthly_cost)

print(f'Your monthly cost is ${monthly_cost:.2f}')
print(f'Your yearly cost is ${yearly_cost:.2f}')
