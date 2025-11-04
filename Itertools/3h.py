from itertools import combinations
l,j=input().split()
l="".join(sorted(l))
j=int(j)
for r in range(1,j+1):
    for p in combinations(l,r):
        print("".join(p))
   