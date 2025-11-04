def frequency_distribution(lst):
    freq={}
    for item in lst:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    return freq
print(frequency_distribution(['a','b','a','c','b','a']))
