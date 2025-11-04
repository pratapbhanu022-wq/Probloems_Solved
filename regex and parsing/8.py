import re
pattern=r"^[789]\d{9}$" 
'''
^ is start of string and  $ is end of string if we dont use them than 
we need to use fullmatch in place of match
'''
for _ in range(int(input())):
    if re.match(pattern,input()):
        print("YES")
    else:
        print("NO")