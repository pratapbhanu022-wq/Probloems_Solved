# Swap Keys and Values in Deeply Nested Dictionary
data = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
swapped = {}
for outer,inner in data.items():
    for k,v in inner.items():
        swapped.setdefault(k,{})[outer]=v
print(swapped) # {'x': {'a': 1, 'b': 3}, 'y': {'a': 2, 'b': 4}}