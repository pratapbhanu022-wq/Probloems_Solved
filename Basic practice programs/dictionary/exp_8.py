# Transpose a Dictionary of Lists
data = {'A': [1, 2], 'B': [3, 4]}
transpose = [dict(zip(data.keys(), values)) for values in zip(*data.values())]
print(transpose) # [{'A': 1, 'B': 3}, {'A': 2, 'B': 4}]
