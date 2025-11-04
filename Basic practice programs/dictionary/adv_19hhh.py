# convert dict of a lists to list of dicts
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
result = [dict(zip(data.keys(), values)) for values in zip(*data.values())]
print(result)
# [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]