# Merge Tuples and Remove Duplicates
t1 = (1, 2, 3)
t2 = (2, 4)
t3 = (3, 5)
res = ()
seen = set()
for x in t1 + t2 + t3:
    if x not in seen:
        res += (x,)
        seen.add(x)
print(res) #(1, 2, 3, 4, 5)
