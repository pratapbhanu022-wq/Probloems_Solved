import math
def is_strong(num):
    return num == sum(math.factorial(int(d)) for d in str(num))
strong_nums = [n for n in range(1, 100000) if is_strong(n)]
print("Strong numbers are:", strong_nums)