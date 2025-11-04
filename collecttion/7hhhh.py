from collections import deque
t=int(input()) # tptal number of test cases
for _ in range(t):
    n=int(input()) # number of cubes
    cubes=deque(map(int,input().split()))
    last=float('inf') # bcoz the very first cube mught be of any size
    possible=True
    while cubes:
        if cubes[0]>=cubes[-1]:
            pick=cubes.popleft()
        else:
            pick=cubes.pop()
        if pick>last:
            possible=False
            break
        last=pick
    print("Yes"if possible else "No")
