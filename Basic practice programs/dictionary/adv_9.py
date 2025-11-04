# merge dict by summing values
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 10}

merged = {}
for k in set(d1) | set(d2):
    merged[k] = d1.get(k, 0) + d2.get(k, 0)
print(merged)