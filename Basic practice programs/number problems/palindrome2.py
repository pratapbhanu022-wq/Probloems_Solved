def is_palin(x:int) ->bool:
    if x<0:
        return False
    if x!=0 and x%10==0:
        return False
    rev_half=0
    while x>rev_half:
        rev_half=rev_half*10+(x%10)
        x//=10
    return rev_half==x or x==rev_half//10 # 1 for even 2 for odd middle digit ignored
i=int(input("Enter number : "))
print(is_palin(i))