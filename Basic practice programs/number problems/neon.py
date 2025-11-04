n=int(input("enter number : "))
p=n**2

if n==1:
    print("1 is always neon")
number=0
while p>0:
    number+=p%10
    p//=10
if number==n:
    print("neon")
else:
    print("not neon")