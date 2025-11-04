# using brute force
n=int(input("Enter a number : "))
if n<=1:
    print("not prime")
else:    
    for i in range(2,int(n+1/2)):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")