from collections import Counter
def ana(a,b):
    count_a=Counter(a) # create a dict holding char as key and repeat as value
    count_b=Counter(b)
    for char in count_a:
        if count_b[char]<count_a[char]:
            return False
    return True
print(ana("abkc","dabcs"))

    