# to solve strict superset problem
A = set(map(int,input().split()))
n=int(input())
result = None
for i in range(n):
    B = set(map(int,input().split()))
    if  A.issuperset(B):
        result=True
    else:
        result=False
print(result)

        
    