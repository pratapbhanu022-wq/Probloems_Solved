# count character in a string
s='programming'
count={}
for ch in s:
    count[ch]=count.get(ch,0)+1
print(count) #{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}


# using counter == most efficient way to do
from collections import Counter
result=Counter(s)
print(result)
Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})