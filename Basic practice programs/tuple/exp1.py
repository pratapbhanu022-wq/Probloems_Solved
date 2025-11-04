# Tuple Deep Swap (Transpose)
data = ((1, 2, 3), (4, 5, 6))
tup=tuple(tuple(col) for col in zip(*data))
print(tup) # ((1, 4), (2, 5), (3, 6))
