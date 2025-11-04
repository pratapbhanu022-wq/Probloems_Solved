def harmonic_sum(n):
    result =0
    if n==1:
        return 1
    if n>1:
        for i in range(1,n+1):
            result+=1/i
        return result
print(round(harmonic_sum(5),2))
