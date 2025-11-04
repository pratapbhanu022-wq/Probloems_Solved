def flip_bits(n):
    b=bin(n)[2:]
    l=[int(digit) for digit in b]
    final=[]
    for i in l:
        if i==1:
            final.append(0)
        else:
            final.append(1)
    deci=int(''.join(map(str,final)),2)
    return deci
print(flip_bits(5))
    

