s = set(map(int,input().split()))
n = int(input())
allsupersets = True
for _ in range(n):

    s1 = set(map(int,input().split()))
    if not s.issuperset(s1):
        allsupersets = False
        break
print(allsupersets)