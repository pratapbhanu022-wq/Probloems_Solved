# hackerrank running from chatgpt
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd = input().split()
    length = int(cmd[1])
    otherset=set(map(int,input().split()))
    if cmd[0]=='intersection_update':
        s.intersection_update(otherset)
    elif cmd[0]=='update':
        s.update(otherset)
    elif cmd[0]=='symmetric_difference_update':
        s.symmetric_difference_update(otherset)
    elif cmd[0]=='difference_update':
        s.difference_update(otherset)
print(sum(s))
'''
# solved by me not accepted on hackerrank
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0]=='intersection_update':
        s.intersection_update(set(map(int, input().split())))
    elif cmd[0]=='update':
        s.update(set(map(int, input().split())))
    elif cmd[0]=='symmetric_difference_update':
        s.symmetric_difference_update(set(map(int, input().split())))
    elif cmd[0]=='difference_update':
        s.difference_update(set(map(int, input().split())))
print(sum(s))
'''