import re


pattern = r'(?=[^aeiouAEIOU]([aeiouAEIOU]{2,})(?=[^aeiouAEIOU]))'
'''
?=[^aeiouAEIOU] = left lookbehind ^ means not so not vowel hence consonant but does not capture it
([aeiouAEIOU]{2,})= the actual match
(?=[^aeiouAEIOU]= right lookahead asserts that after our match there is something
'''

s = input()


matches = re.findall(pattern, s)

if matches:
    for match in matches:
        print(match)

else:
    print(-1)
