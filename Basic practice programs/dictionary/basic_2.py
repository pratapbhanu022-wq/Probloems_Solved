# count frequency of each element in a list
nums=[1,1,1,1,2,2,2,3,4,4,5,6,7,7,7,7]
freq={}
for n in nums:
    freq[n]=freq.get(n,0)+1 # n is key means value = item of the list
    # freq.get(n,0)+1 returns current count if n exist as a key otheerwise 0.
print(freq) # output = {1: 4, 2: 3, 3: 1, 4: 2, 5: 1, 6: 1, 7: 4}


# using collection counter for same list
from collections import Counter
freq=Counter(nums)
print(freq) # print sorted output=Counter({1: 4, 7: 4, 2: 3, 4: 2, 3: 1, 5: 1, 6: 1})
print(freq.most_common()) #.......... 
# sorted list o/p=[(1, 4), (7, 4), (2, 3), (4, 2), (3, 1), (5, 1), (6, 1)]


# using default dict
from collections import defaultdict
frq=defaultdict(int) # default value=0
for n in nums:
    frq[n]+=1
print(frq) # o/p=defaultdict(<class 'int'>, {1: 4, 2: 3, 3: 1, 4: 2, 5: 1, 6: 1, 7: 4})