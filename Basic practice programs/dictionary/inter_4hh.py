# group words by their length
d=['banana','apple','car','cow','ball']
grouped={}
for word in d:
    grouped.setdefault(len(word),[]).append(word)
print(grouped) # {6: ['banana'], 5: ['apple'], 3: ['car', 'cow'], 4: ['ball']}