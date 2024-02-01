"""
Компания — разработчик программного обеспечения продает программный пакет, который реализуется в рознице за 99 долларов.
 Скидки за количество предоставляются в соответствии со списком ниже:
 10-19 штук - скидка 10%
 20-49 штук - скидка 20%
 50-99 штук - скидка 30%
 более 100 штук - скидка 40%

Напишите программу, которая просит пользователя ввести количество приобретенных пакетов. Программа должна затем показать
сумму скидки (если таковая имеется) и общую сумму покупки после вычета скидки.
"""

price = 100
packages = 200

if 0 < packages < 10:
    # 10%
    discount = 0
    total = price * packages - discount
elif 10 <= packages <= 19:
    discount = price * 0.1 * packages
    total = price * packages - discount
elif 20 <= packages <= 49:
    discount = price * 0.2 * packages
    total = price * packages - discount
elif 50 <= packages <= 99:
    discount = price * 0.3 * packages
    total = price * packages - discount
else:
    discount = price * 0.4 * packages
    total = price * packages - discount

print(f"Total cost: ${total:.2f}\n"
      f"Discount: ${discount:.2f}")
