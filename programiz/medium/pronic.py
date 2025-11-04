def is_pronic(n):
    for i in range(int(n**0.5) + 1):
        if i * (i + 1) == n:
            return True
    return False

num = 6
if is_pronic(num):
    print(num, "is a pronic number")
else:
    print(num, "is not a pronic number")