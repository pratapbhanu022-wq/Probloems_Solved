# Nested update — increment a nested value safely
data = {'a': {'x': 5}, 'b': {}}
key, subkey = 'b', 'x'
data.setdefault(key, {}).setdefault(subkey, 0)
data[key][subkey] += 10
print(data)
# {'a': {'x': 5}, 'b': {'x': 10}}