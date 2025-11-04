def baum_sweet(n):
    if n == 0:
        return 1
    binary = bin(n)[2:]  # binary string
    zero_blocks = binary.split('1')
    for block in zero_blocks:
        if len(block) % 2 == 1 and len(block) != 0:
            return 0
    return 1
sequence = [baum_sweet(i) for i in range(10)]
print(sequence)