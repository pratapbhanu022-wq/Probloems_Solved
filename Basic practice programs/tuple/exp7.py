#Frequency Count Using Tuple
t = (1, 2, 1, 3, 2, 1)
count = {}
for x in t:
    count[x] = count.get(x, 0) + 1
print(count) #{1: 3, 2: 2, 3: 1}
