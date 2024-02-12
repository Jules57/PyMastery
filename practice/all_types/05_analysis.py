sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

d = {}

for i in keys:
    d[i] = sample_dict[i]

print(d)
