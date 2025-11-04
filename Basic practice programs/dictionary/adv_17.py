# Count total number of items in nested dictionary
data = {'A': {'x': 1, 'y': 2}, 'B': {'p': 3, 'q': 4, 'r': 5}}
count = sum(len(v) for v in data.values())
print(count)
# 5