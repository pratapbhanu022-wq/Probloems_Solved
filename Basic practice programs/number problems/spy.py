n=int(input("Enter a number : "))
sum=0
mul=1
while n>0:
    digit=n%10
    sum+=digit
    mul*=digit
    n//=10
if sum==mul:
    print("spy")
else:
    print("not")