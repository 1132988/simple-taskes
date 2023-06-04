dict1 = {1: 5, 2: 4, 3: 10}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict)