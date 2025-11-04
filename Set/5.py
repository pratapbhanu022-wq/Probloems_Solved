n = list(map(int,input().split()))
array = list(map(int,input().split()))
length = len(array)
A = set(map(int,input().split()))
B = set(map(int,input().split()))
Happiness = 0
for i in range(length):
    if array[i] in A:
        Happiness+=1
    elif array[i] in B:
        Happiness-=1
print(Happiness)
'''
to count the happiness of user using sets
'''
