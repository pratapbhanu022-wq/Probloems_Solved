n=int(input("enter number: "))
p=n**2
l=len(str(n))
q=[]
for i in range(l):
    digit=p%10
    q.append(digit)
    p//=10
q.reverse()
final=int(''.join(map(str,q)))
if final==n:
    print("auto")
else:
    print("not")
'''
# without string
num = int(input("Enter a number: "))
square = num ** 2

# Count digits of the number
temp = num
count = 0
while temp > 0:
    count += 1
    temp //= 10

# Extract last 'count' digits of square
last_digits = square % (10 ** count)

if last_digits == num:
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number")
'''
'''
# using string
num = int(input("Enter a number: "))
square = num ** 2

# Check if square ends with the number itself
if str(square).endswith(str(num)):
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number")

'''

    