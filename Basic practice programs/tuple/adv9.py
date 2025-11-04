# Partition Tuple by Condition
t = (1, 2, 3, 4)
evens, odds = (), ()
for x in t:
    if x % 2 == 0:
        evens += (x,)
    else:
        odds += (x,)
print(evens, odds) # (2, 4) (1, 3)
