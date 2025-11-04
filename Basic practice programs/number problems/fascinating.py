num = int(input("Enter a number: "))

# concatenate num, num*2, num*3
concat = str(num) + str(num*2) + str(num*3)

# check condition
if ''.join(sorted(concat)) == '123456789':
    print(num, "is a Fascinating number")
else:
    print(num, "is not a Fascinating number")