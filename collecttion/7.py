from collections import Counter
s=input()
count=Counter(s)
sorted_count = dict(sorted(count.items(),key=lambda x:(-x[1],x[0])))
'''
here count.items=[('b',3),('a',2),('c',2),('d',1),('e',1)] it gives a key-value pair
key=lambda x:(-x[1],x[0]) here x is each tuple('c'2) for eg in this x[1]=2,x[0]=c
-x[1] is done to return a negative frequency bcoz sorting is done in desending order
-3 -2 -2 -1 -1 
by default in python sorting is done in asending order but if we use -x[1] , than 
highest negative value become lowest so it is sorted in descending order
'''
top3=list(sorted_count.items())[:3]
for k,v in top3:
    print(k,v)