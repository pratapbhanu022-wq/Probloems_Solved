def can_type(keys, word):
    for w in word:
        if w not in keys:
            return False
    else:
        return True
print(can_type('abc','bad'))