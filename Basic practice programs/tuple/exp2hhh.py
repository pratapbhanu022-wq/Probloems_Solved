# Flatten Deeply Nested Tuple
def flatten(t):
    res = ()
    for x in t:
        if isinstance(x, tuple):
            res += flatten(x)
        else:
            res += (x,)
    return res
print(flatten((1, (2, (3, (4, (5,)))))))
# (1, 2, 3, 4, 5)
