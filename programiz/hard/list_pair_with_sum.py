from itertools import product
def find_pairs(lst1,lst2,x):
    final=list(product(lst1,lst2))
    result=[]
    for i in final:
        if i[0]+i[1]==x:
            result.append(i)
    return result
print(find_pairs([1,2,3],[2,3,4],5))
    