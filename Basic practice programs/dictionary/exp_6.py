# find most common character in a string
s = "successes"
freq = {ch: s.count(ch) for ch in set(s)}
most_common = max(freq, key=freq.get)
print(freq) # {'s': 4, 'e': 2, 'u': 1, 'c': 2}
print(most_common, freq[most_common]) # s 4
