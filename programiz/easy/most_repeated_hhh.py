def most_repeated(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    return max(freq,key=freq.get)
print(most_repeated("hello world"))
    