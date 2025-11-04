import re
m=re.search(r"([a-zA-Z0-9])\1+",input()) 
'''
in expression (...) capture the matched character in a group(group 1)
\1 a backreference. it means " the same texted matched by group 1" for ex. if "a" is captured
than \1 means "a"
+ is for one or more repeatation
'''
if m:
    print(m.group(1))
else:
    print(-1)