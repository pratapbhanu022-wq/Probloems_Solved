def type_with_broken_keyboard(word):
    result=""
    vowels="AEIOUaeiou"
    lowercase=True
    for char in word:
        if char in vowels:
            lowercase=not lowercase
        if lowercase:
            result+=char.lower()
        else:
            result+=char.upper()
        
    return result
print(type_with_broken_keyboard("banana"))