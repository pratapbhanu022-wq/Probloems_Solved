from itertools import product
K,M=map(int,input().split())
lists=[]
for i in range(K):
    data = list(map(int,input().split()))
    arr = data[1:]
    lists.append([(x*x)%M for x in arr])
best = 0
for combo in product(*lists):
    s=sum(combo)%M
    if s>best:
        best = s
print(best)

