# invert a dict with duplicate values
data = {'a': 1, 'b': 2, 'c': 1}
inverse = {}
for k, v in data.items():
    inverse.setdefault(v, []).append(k)
print(inverse) # {1: ['a', 'c'], 2: ['b']}