sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

mm = min(sample_dict.values())

res = [key for key in sample_dict if sample_dict[key] == mm]

print(res[0])
