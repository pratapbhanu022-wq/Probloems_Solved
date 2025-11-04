def move_zeroes_to_end(n):
    c=0
    temp=n
    while temp>0:
        if temp%10==0:
            c+=1
        temp//=10
    s=str(n)
    s=s.replace("0","")
    m=int(s)
    result=m*(10**c)
    return result
print(move_zeroes_to_end(1020304050))   
'''
def move_zeroes_to_end(n):
    s = str(n)
    count_zeros = s.count('0')
    non_zero_digits = s.replace('0', '')
    result = non_zero_digits + '0' * count_zeros
    return int(result)
print(move_zeroes_to_end(1020304050)) # Output: 12345

''' 