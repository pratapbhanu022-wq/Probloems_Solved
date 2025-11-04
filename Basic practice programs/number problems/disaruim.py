num = int(input("Enter a number: "))
s = str(num)
length = len(s)
total = 0
for i in range(length):
    total += int(s[i]) ** (i + 1)
if total == num:
    print(num, "is a Disarium number")
else:
    print(num, "is not a Disarium number")