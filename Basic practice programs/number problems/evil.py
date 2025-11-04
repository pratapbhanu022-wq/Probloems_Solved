num = int(input("Enter a number: "))

# convert to binary (remove '0b' prefix)
binary = bin(num)[2:]

# count number of 1s
count_ones = binary.count('1')

print("Binary representation:", binary)

if count_ones % 2 == 0:
    print(num, "is an Evil number")
else:
    print(num, "is not an Evil number (Odious number)")