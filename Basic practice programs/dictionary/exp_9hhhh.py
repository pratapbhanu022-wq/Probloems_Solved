# Word Frequency Across Multiple Documents
docs = [
    "python code easy",
    "python dictionary example code",
    "easy code problems"
]

word_count = {}
for i, doc in enumerate(docs, 1):
    for word in doc.split():
        word_count.setdefault(word, {}).setdefault('count', 0)
        word_count[word]['count'] += 1
        word_count[word].setdefault('appears_in', []).append(i)

print(word_count)
'''
{'python': {'count': 2, 'appears_in': [1, 2]}, 'code': {'count': 3, 'appears_in': [1, 2, 3]}, 'easy': {'count': 2, 'appears_in': [1, 3]}, 'dictionary': 
{'count': 1, 'appears_in': [2]}, 'example': {'count': 1, 'appears_in': [2]}, 'problems': {'count': 1, 'appears_in': [3]}}
'''
