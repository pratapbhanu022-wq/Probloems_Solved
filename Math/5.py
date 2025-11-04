a=int(input())
b=int(input())
result=divmod(a,b)
answer= tuple(result)
for item in answer:
    print(item)
print(result)