"""
Налог на недвижимое имущество. Муниципальный округ собирает налоги на недвижимое имущество на основе оценочной
стоимости имущества, составляющей 60% его фактической стоимости. Например, если акр земли оценен в 10 000 долларов,
то его оценочная стоимость составит 6000 долларов. В этом случае налог на имущество составит 72 цента за каждые 100
долларов оценочной стоимости. Налог на акр, оцененный в 6000 долларов, составит 43.20 доллара. Напишите программу,
которая запрашивает фактическую стоимость недвижимого имущества и показывает оценочную стоимость и налог на
имущество.
"""


TAX_RATE = .6
TAX_ITEM = 100
RATE_PER_TAX_ITEM = .72


def get_estimation_cost(cost: float) -> float:
    return cost * TAX_RATE


def get_estate_tax(estimated_amount: float) -> float:
    return estimated_amount / TAX_ITEM * RATE_PER_TAX_ITEM


actual_price = float(input('Enter the actual cost of your real estate: '))
estimated_cost = get_estimation_cost(actual_price)
estate_tax = get_estate_tax(estimated_cost)
print(f'The estimated cost is ${estimated_cost:.2f}')
print(f'The real estate tax is ${estate_tax:.2f}')
