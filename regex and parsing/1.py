'''
# without using regex 
t=int(input())
for i in range(t):
    n=input()
    if '.' in n:
        try:
            n=float(n)
            print(True)
        except:
            print(False)
    else:
        print(False)
'''
# using regex
import re
for _ in range(int(input())):
    print(bool(re.fullmatch(r"[+-]?\d*\.\d+",input())))