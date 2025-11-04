# Count Occurrences Without Counter
t = (1, 2, 1, 3, 2)
freq = {}
for x in t:
    freq[x] = freq.get(x, 0) + 1
print(freq) # {1: 2, 2: 2, 3: 1}
