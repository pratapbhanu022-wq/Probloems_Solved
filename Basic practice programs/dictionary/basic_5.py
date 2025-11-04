# remove keys with specific values from a dict
data={'a':0,'b':4,'c':0,'d':7}
new={k:v for k,v in data.items() if v!=0}
print(new) # o/p={'b': 4, 'd': 7}