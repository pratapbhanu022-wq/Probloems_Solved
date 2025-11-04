def sum_of_smallest(numbers):
    numbers.sort()
    sum_two=numbers[0]+numbers[1]
    return sum_two
print(sum_of_smallest([21,8,12,18,22]))