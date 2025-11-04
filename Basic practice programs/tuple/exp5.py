'''
Rotate Tuple
Problem:
Rotate tuple elements n positions to the right.
'''
t = (1, 2, 3, 4, 5)
n = 2
rotated = t[-n:] + t[:-n]
print(rotated) # (4, 5, 1, 2, 3)
