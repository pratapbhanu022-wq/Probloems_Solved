# Update Tuple Immutably
t = (1, 2, 3, 4, 5)
new_t = t[:2] + (99,) + t[3:]
print(new_t) # (1, 2, 99, 4, 5)
