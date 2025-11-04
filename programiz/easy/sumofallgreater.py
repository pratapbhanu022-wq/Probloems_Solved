def sum_greater_than(numbers, n):
    s=0
    for i in numbers:
        if i>n:
            s+=i
    return s
print(sum_greater_than([1,2,3,4,5,6],3))
    