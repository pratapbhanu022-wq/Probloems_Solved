n=int(input("Enter the number: "))
total=0
for i in range(1,(n//2)+1):
    if n%i==0:
        total+=i
if total==n:
    print("perfact ")
else:
    print("not perfact")

