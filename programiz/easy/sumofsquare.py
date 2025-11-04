def sum_of_squares(numbers):
    sum=0
    for i in numbers:
        sum+=i**2
    return sum
print(sum_of_squares([2,3,4,1]))