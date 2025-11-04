# Program to check Xylem or Phloem number

num = int(input("Enter a number: "))

n = num
last = n % 10        # last digit
sum_extreme = last
sum_mean = 0

# remove last digit
n //= 10

while n > 9:         # loop till second digit
    digit = n % 10
    sum_mean += digit
    n //= 10

first = n            # first digit
sum_extreme += first

if sum_extreme == sum_mean:
    print(num, "is a Xylem number.")
else:
    print(num, "is a Phloem number.")