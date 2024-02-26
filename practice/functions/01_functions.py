"""
Конвертер километров. Напишите программу, которая просит пользователя ввести расстояние в километрах и затем это
расстояние преобразует в мили. Формула преобразования:
   miles = km х 0.6214.
"""
CONVERSION_FACTOR = 0.6214


def convert_km_to_miles(kilometers: float) -> float:
    """This function return miles from kilometers."""
    return kilometers * CONVERSION_FACTOR


def validate_input() -> float:
    is_valid = 'yes'
    distance_in_km = input('Enter the distance in kilometers: ')

    while is_valid != 'no':
        if distance_in_km.isalpha():
            distance_in_km = input('Enter the distance in kilometers: ')
            continue

        if float(distance_in_km) >= 0:
            return float(distance_in_km)
        else:
            distance_in_km = input('Enter the distance in kilometers: ')


km = validate_input()

miles = convert_km_to_miles(km)
print(f'The distance in miles is {miles:.2f}')
