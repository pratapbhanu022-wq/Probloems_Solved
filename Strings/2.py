def split_and_join(line):
    l=line.split(" ")
    k="-".join(l)
    return k
    


line = input()
result = split_and_join(line)
print(result)