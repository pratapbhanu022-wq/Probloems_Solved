# given a list , return a dict of freq sorted in descnding order
nums = [4, 2, 2, 3, 4, 4, 1, 3, 2]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

# Sort by frequency (descending), then by element value
sorted_freq = dict(sorted(freq.items(), key=lambda x: (-x[1], x[0])))
print(sorted_freq) # {2: 3, 4: 3, 3: 2, 1: 1}