'''
Frequency-Based Key Removal

Problem: Remove dictionary keys that appear less than 2 times in values.
'''
data = {'a': [1,2,3], 'b': [2,3], 'c': [3,4], 'd': [5]}
count = {}
for v in data.values():
    for x in v:
        count[x] = count.get(x, 0) + 1

filtered = {k:v for k,v in data.items() if any(count[x] > 1 for x in v)}
print(filtered) # {'a': [1, 2, 3], 'b': [2, 3], 'c': [3, 4]}
