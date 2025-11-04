# find common keys in 2 dict
a = {'x': 1, 'y': 2, 'z': 3}
b = {'y': 5, 'z': 7, 'w': 9}
common = a.keys() & b.keys()
print(common)