'''
Find Max by Custom Rule
Problem:
Given tuples (value, weight), find item with highest value-to-weight ratio.
'''
items = ((10, 2), (5, 1), (8, 4))
best = max(items, key=lambda x: x[0]/x[1])
print(best) # (10, 2)
