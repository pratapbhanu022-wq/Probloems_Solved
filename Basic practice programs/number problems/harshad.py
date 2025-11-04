n=int(input("Enter the number: "))
m=n
total=0
while m>0:
    digit=m%10
    total+=digit
    m//=10
if n%total==0:
    print("harshad")
else:
    print("not harshad")

