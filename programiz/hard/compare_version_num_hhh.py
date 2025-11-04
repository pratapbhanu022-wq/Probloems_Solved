def compareVersion(v1, v2):
    v1_parts = v1.split('.')
    v2_parts = v2.split('.')
    max_len = max(len(v1_parts), len(v2_parts))
    v1_parts += ['0'] * (max_len - len(v1_parts))
    v2_parts += ['0'] * (max_len - len(v2_parts))
    for a, b in zip(v1_parts, v2_parts):
        a, b = int(a), int(b)
        if a < b:
            return -1
        elif a > b:
            return 1
    return 0
print(compareVersion("1.01", "1.001"))  