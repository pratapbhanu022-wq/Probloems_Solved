from itertools import product
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
result = [(a,b) for a,b in product(l1,l2)]
print(*result) # * gives item without[]