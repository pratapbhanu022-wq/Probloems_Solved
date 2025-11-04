from itertools import permutations
l,j=input().split()
for p in sorted(permutations(l,int(j))):
    print("".join(p))
   