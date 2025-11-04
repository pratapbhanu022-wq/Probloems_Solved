# Count Word Lengths in a Sentence
sentence = "python makes coding fun and interesting"
length_count = {}
for word in sentence.split():
    length_count[len(word)] = length_count.get(len(word), 0) + 1
print(length_count)
# {6: 2, 5: 1, 3: 2, 11: 1}