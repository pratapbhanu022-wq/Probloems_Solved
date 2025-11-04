# sort dictionary by values
scores={'bhanu':85,'abhi':90,'alok':67}
new=dict(sorted(scores.items(),key=lambda x:x[1]))
print(new) # output={'alok': 67, 'bhanu': 85, 'abhi': 90}