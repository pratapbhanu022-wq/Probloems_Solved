# Nested Tuple to Dictionary Conversion
pairs = (("x", 1), ("y", 2), ("z", 3))
d = {k: v for k, v in pairs}
print(d) # {'x': 1, 'y': 2, 'z': 3}
