def find_anagram(text, word):
    # clean text: remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    word = word.lower()

    word_len = len(word)
    sorted_word = sorted(word)

    # slide a window over the text
    for i in range(len(text) - word_len + 1):
        substring = text[i:i + word_len]
        if sorted(substring) == sorted_word:
            return substring

    return "Anagram not found"
print(find_anagram("The quick brown fox jumps over the lazy dog", "god"))