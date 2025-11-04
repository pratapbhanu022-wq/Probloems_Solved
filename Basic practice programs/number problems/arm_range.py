lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Armstrong numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    n = len(str(abs(num)))
    total = sum(int(digit) ** n for digit in str(abs(num)))
    if total == abs(num):
        print(num)