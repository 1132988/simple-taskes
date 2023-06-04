import heapq
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(heapq.nlargest(3, my_dict, key=lambda k: my_dict[k]))