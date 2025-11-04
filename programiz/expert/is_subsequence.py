# is subsequence
def is_subsequence(s, t):
    ind=0
    i=0
    while (ind<len(s) and i<len(t)):
        if (t[i]==s[ind]):
            ind+=1
        i+=1
    if (ind==len(s)):
        return True
    else:
        return False
print(is_subsequence("abc","ahbgdc"))