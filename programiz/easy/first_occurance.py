def fo(s):
    for i in s:
        if s.count(i)==1:
            return i
    return ""
print(fo("hello world"))