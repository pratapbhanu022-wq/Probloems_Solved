from itertools import combinations_with_replacement
l,j=input().split()
l="".join(sorted(l))
j=int(j)
for p in combinations_with_replacement(l,j):
    print("".join(p))