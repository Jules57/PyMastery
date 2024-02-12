BABY_PRICE = 0.00
CHILD_PRICE = 14.00
ADULT_PRICE = 23.00
SENIOR_PRICE = 18.00

BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

total = 0

line = input("Enter the age of the guest (blank line to exit): ")

while line != "":
    age = int(line)

if age <= BABY_LIMIT:
    total = total + BABY_PRICE
elif age <= CHILD_LIMIT:
    total = total + CHILD_PRICE
elif age <= ADULT_LIMIT:
    total = total + ADULT_PRICE
else:
    total = total + SENIOR_PRICE

line = input("Enter the age of the guest (blank line to exit): ")

print(f"The total cost for this group is ${total:.2f}.")
