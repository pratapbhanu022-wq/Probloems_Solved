def fact(i):
    fac=1
    for j in range(1,i+1):
       fac*=j
    return fac
n=int(input("Enter number : "))
total=sum(fact(int(digit)) for digit in str(n))
if total==n:
    print("strong number")
else:
    print("not strong number")
'''
import math
n = int(input("Enter number: "))
total = sum(math.factorial(int(digit)) for digit in str(n))
if total == n:
    print("strong number")
else:
    print("not strong number")
'''
'''
import math

def is_strong(num):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)  # factorial of each digit
        temp //= 10
    
    return total == num

# Example usage
num = 145
if is_strong(num):
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")

'''