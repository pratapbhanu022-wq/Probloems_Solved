import os
def solve(s):
    words = s.split(' ') # using split(' ') instead of split('') keeps the
    # extra space there in name if we use second one than a name like
    # jhon    doe will become Jhon Doe and extra space will be removed
    cap= [w[0].upper() + w[1:] if w else '' for w in words]
    return ' '.join(cap)
if __name__=='__main__':
    
    s=input()
    result=solve(s)
    print(result)