# Group Anagrams Using Dictionary
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
grp={}
for w in words:
    key=''.join(sorted(w))
    grp.setdefault(key,[]).append(w)
print(list(grp.values()))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]