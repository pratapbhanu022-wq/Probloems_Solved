# using square root optimization
import math
n=int(input("Enter a number : "))
if n<=1:
    print("not prime")
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")
            