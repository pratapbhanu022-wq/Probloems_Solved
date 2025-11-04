def replace_vowels(st, replacement='*'):
    new_str = ''
    for char in st:
        if char in 'aeiouAEIOU':
            new_str += replacement
        else:
            new_str += char
    return new_str

result = replace_vowels("Hello World", '*')
print(result)  # Output: H*ll* W*rld
