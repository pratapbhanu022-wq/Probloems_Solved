n=int(input("enter number: "))
m=n**2
d=len(str(n))
right=m%(10**d)
left=m//(10**d)
if right+left==n:
    print('kaprekar')
else:
    print('not')