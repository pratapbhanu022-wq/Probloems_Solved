from itertools import combinations
n = int(input())
l = input().split()
k=int(input())
comb=list(combinations(l,k))
count = 0
for c in comb:
    if 'a' in c:
        count+=1
probability=count/len(comb)
print(probability)
