# create dictionary of frequencies of words from a sentence
text = "python is fun and python is powerful and easy"
words = text.split()
freq = {word: words.count(word) for word in set(words)}
print(freq) # {'is': 2, 'python': 2, 'fun': 1, 'easy': 1, 'powerful': 1, 'and': 2}