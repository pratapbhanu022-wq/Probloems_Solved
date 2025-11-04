# Combine list of dictionaries by a key
data = [
    {'id': 1, 'score': 10},
    {'id': 2, 'score': 5},
    {'id': 1, 'score': 7},
    {'id': 2, 'score': 3}
]

result = {}
for d in data:
    result[d['id']] = result.get(d['id'], 0) + d['score']

print(result) # {1: 17, 2: 8}
