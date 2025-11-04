# Tuple as Dictionary Keys
cells = [(0, 0), (0, 1), (0, 0)]
d = {}
for c in cells:
    d[c] = d.get(c, 0) + 1
print(d) # {(0, 0): 2, (0, 1): 1}
