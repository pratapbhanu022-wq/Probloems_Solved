M = int(input())
M_set = set(map(int, input().split()))
N = int(input())
N_set = set(map(int, input().split()))
U= M_set.union(N_set)
I=M_set.intersection(N_set)
D= U.difference(I)
for n in sorted(D):
    print(n)
# symmetric difference