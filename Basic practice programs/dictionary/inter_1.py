# invert a dict(swap key and values)
data={'a':0,'b':4,'c':0,'d':7}
d={v:k for k,v in data.items()}
print(d) #op={0: 'c', 4: 'b', 7: 'd'} first pair is droped bcoz
# duplicate keys are not allowed and only last value is retained