import re
m=[]
for _ in range(int(input())):
    l=re.findall(r"\#[0-9a-fA-F]{3,6}(?=\S)",input())
    if l:
        m.append(l)
for i in m:
    for j in i:
        print(j)