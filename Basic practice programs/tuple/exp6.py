# Group by Tuple Keys
data = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
res = {}
for k, v in data:
    res.setdefault(k, ())
    res[k] += (v,)
print(res) # {'a': (1, 3), 'b': (2, 4)}
