# Tuple Difference Tracker
t1 = (0, 2, 3, 4)
t2 = (1, 3, 3, 5)
diff = tuple(i for i in range(len(t1)) if t1[i] != t2[i])
print(diff) #(0, 1, 3)
