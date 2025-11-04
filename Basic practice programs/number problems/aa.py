n=int(input("enter number: "))
p=n**2
m=str(n)
q=str(p)
if q[-len(m):]==m:
    print("automorphic")
else:
    ("not")