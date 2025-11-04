'''
# using string
num = int(input("Enter a number: "))
cube = num ** 3
if str(cube).endswith(str(num)):
    print(num, "is an trimorphic number")
else:
    print(num, "is not an trimorphic number")
'''
# without string
num = int(input("Enter a number: "))
cube = num ** 3
count=0
temp=num
while temp>0:
    count+=1
    temp//=10
digits=cube%(10**count)
if num==digits:
    print("trimorphic")
else:
    print("not trimorphic")