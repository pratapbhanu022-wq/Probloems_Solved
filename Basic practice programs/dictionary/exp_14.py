# Nested Sum — Compute Total Sum of All Nested Values
data = {
    'A': {'x': 10, 'y': 20},
    'B': {'x': 5, 'y': 15, 'z': 10}
}
total_sum = sum(sum(inner.values()) for inner in data.values())
print(total_sum) # 60
