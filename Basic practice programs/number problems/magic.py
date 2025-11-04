def is_magic(n: int) -> bool:
    if n <= 0:
        return False
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n == 1

# demo
num = int(input("Enter a number: "))
print("Magic" if is_magic(num) else "Not magic")