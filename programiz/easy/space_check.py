def has_spaces(s):
    for i in s:
        if i==" ":
            return True
    else:
        return False
        
print(has_spaces("Hello world"))