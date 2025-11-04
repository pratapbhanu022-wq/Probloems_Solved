n=int(input("enter a number: "))
'''

for digit in str(n):
    if digit =='0':
        print("duck")
        break
else:
        print("not duck")
'''
while n>0:
    digit=n%10
    if digit==0:
        print("duck")
        break
    n//=10
else:
    print("not duck")
