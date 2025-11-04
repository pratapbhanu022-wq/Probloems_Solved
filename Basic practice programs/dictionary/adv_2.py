# convert a list of dict to a combined dict
data=[{'a':10},{'b':20},{'c':30}]
merged={}
for d in data:
    merged.update(d)
print(merged) # {'a': 10, 'b': 20, 'c': 30}