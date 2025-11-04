x,k = map(int,input().split())
print(eval(input()) == k)
# x=1 k=4
# input=x**3 + x**2 + x + 1 eval is discoureged to use bcoz of security reasons
# if the equation is true print true else false
'''
# same code with different approach
x,k=list(map(int,input().split()))
l=input()
    
result=eval(l)
if result==k:
    print(True)
else:
    print(False)
'''