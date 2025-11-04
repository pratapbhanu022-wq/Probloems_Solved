m=int(input("Enter number : "))
n=abs(m)
l=len(str(n))
total=0
while n>0:
    digit=n%10
    total+=digit**l
    n//=10
if total==abs(m):
    print("number is armstrong")
else:
    print("its not")
    