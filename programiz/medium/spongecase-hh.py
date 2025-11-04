def to_spongecase(text):
    s=""
    for i,ch in enumerate(text):
        if i%2==0:
            s+=ch.lower()
        else:
            s+=ch.upper()
    return s
print(to_spongecase("programizpro123"))


    