"""
Оценщик малярных работ. Малярная компания установила, что на каждые 10 квадратных метров поверхности стены требуется
   5 литров краски и 8 часов работы. Компания взимает за работу 20 долларов в час. Напишите программу, которая просит
   пользователя ввести площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски. Программа должна
   показать следующие данные:
   • количество требуемых емкостей краски:
   • количество затраченных рабочих часов;
   • стоимость краски;
   • стоимость работы;
   • общая стоимость малярных работ.
"""

import math


SURFACE_UNIT = 10
PAINT_VOLUME_PER_SURFACE_UNIT = 5
LITRES_PER_PAINT_BUCKET = 5
WORK_TIME_PER_SURFACE_UNIT = 8
PAYMENT_RATE_PER_HOUR = 20


def calculate_paint_buckets(area):
    return math.ceil((area * PAINT_VOLUME_PER_SURFACE_UNIT / SURFACE_UNIT) / LITRES_PER_PAINT_BUCKET)


def calculate_hours(area):
    return area / SURFACE_UNIT * WORK_TIME_PER_SURFACE_UNIT


def calculate_paint_cost(buckets, bucket_cost):
    return buckets * bucket_cost


def calculate_work_cost(hours):
    return hours * PAYMENT_RATE_PER_HOUR


def calculate_total_cost(paint, hours):
    return paint + hours


area_to_paint = 60
paint_cost_per_bucket = 12

paint_buckets = calculate_paint_buckets(area_to_paint)
work_hours = calculate_hours(area_to_paint)
paint_cost = calculate_paint_cost(paint_buckets, paint_cost_per_bucket)
work_cost = calculate_work_cost(work_hours)
total_cost = calculate_total_cost(paint_cost, work_cost)

print(f'Paint buckets: {paint_buckets} buckets,\n'
      f'Work hours: {work_hours} hours,\n'
      f'Paint cost: ${paint_cost:.2f},\n'
      f'Work cost: ${work_cost:.2f},\n'
      f'Total cost: ${total_cost:.2f}.')
