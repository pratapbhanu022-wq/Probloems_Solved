# to find captains room
# this method works only if repeated number are not exact same
'''
N=int(input())
rooms = list(map(int,input().split))
unique=None
for x in set(rooms):
    if rooms.count(x)==1:
       unique=x
       break
print(unique)
'''
# if repeat number are same for eg. if 2 is repeated 5 times and 4 is 
# repeated 5 time as well and 7 is unique in this case this method will 
# work
k=int(input())
rooms = list(map(int,input().split()))
unique=(sum(set(rooms))*k-sum(rooms))//(k-1)
print(unique)
