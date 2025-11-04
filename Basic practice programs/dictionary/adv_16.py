# Find keys having maximum and minimum values
data = {'x': 10, 'y': 25, 'z': 5}
max_key = max(data, key=data.get)
min_key = min(data, key=data.get)
print(f"Max: {max_key} → {data[max_key]}, Min: {min_key} → {data[min_key]}")

# Max: y → 25, Min: z → 5