from collections import deque
n=int(input())
de=deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0]=='append':
        de.append(int(cmd[1]))
    elif cmd[0]=='appendleft':
        de.appendleft(int(cmd[1]))
    elif cmd[0]=='pop':
        de.pop()
    elif cmd[0]=='popleft':
        de.popleft()
print(*de) # to convert into a string and than print it