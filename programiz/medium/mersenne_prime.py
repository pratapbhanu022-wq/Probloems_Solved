def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def mersenne(n):
    j=1
    res=[]
    while 2**j-1<=n:
        
        if is_prime(2**j-1):
            res.append(2**j-1)
        j+=1
    return res
print(mersenne(130))




