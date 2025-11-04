n=int(input())
c=0
if n==1:
    c=1
else:
    while n>0:
        n//=10 # //10 is integer division it removes last digit
        c+=1
print(c)
'''
import math
n=int(input())
c=0
if n==1:
    c=1
else:
    c=int(math.log10(abs(n))) + 1
print(c)

'''