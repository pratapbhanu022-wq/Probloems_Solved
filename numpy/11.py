import numpy as np
n,m = map(int,input().split())

l1 = []
for i in range(n):
    l1.append(list(map(int, input().split())))

arr = np.array(l1)

print(np.mean(arr, axis =1))
print(np.var(arr, axis = 0))
print(round(np.std(arr, axis = None),11))