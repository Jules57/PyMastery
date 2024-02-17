# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
#
# mm = min(sample_dict.values())
#
# res = [key for key in sample_dict if sample_dict[key] == mm]
#
# print(res[0])

resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)

res_list = []
for elem in ['Hello ', 'Good']:
    for char in ['Dear', 'Bye']:
        res_list.append(elem + char)

print(res_list)
