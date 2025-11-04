import re
s=input()
k=input()
flag=False
for i in re.finditer(rf'(?=({k}))',s):
    # ? for 0 or 1 occurence 
    print((i.start(1),i.end(1)-1))
    # start(1) means first group in this case there is only one group 
    # for a better understanding a group of 2 is r'(p=)(\d+) here (p=) is first and (\d+) is second 
    flag=True
if not flag:
    print((-1,-1))