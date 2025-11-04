def ginortS(s):
    lower = sorted([ch for ch in s if ch.islower()])
    upper = sorted([ch for ch in s if ch.isupper()])
    odd = sorted([ch for ch in s if ch.isdigit() and int(ch) % 2 == 1])
    even = sorted([ch for ch in s if ch.isdigit() and int(ch) % 2 == 0])
    p=''.join(lower + upper + odd + even)
    return p
print(ginortS('Sorting1234'))