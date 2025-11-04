# Build an Index of Words in a Sentence List
sentences = [
    "python is fun",
    "java and python",
    "c is powerful"
]

index = {}
for i, s in enumerate(sentences,1):
    for word in s.split():
        index.setdefault(word, []).append(i)

print(index)
'''
{'python': [1, 2], 'is': [1, 3], 'fun': [1], 'java': [2], 'and': [2], 'c': [3], 'powerful': [3]}
'''