# Create a dictionary from string character pairs
s = "aabbccaa"
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
print(count) # {'a': 4, 'b': 2, 'c': 2}
