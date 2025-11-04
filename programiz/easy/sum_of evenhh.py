def sum_of_evens(matrix):
    flat = [ x for row in matrix for x in row]
    s=0
    for i in flat:
        if i%2==0:
            s+=i
    return s
l=[[1,2,3],[4,5,6],[7,8,9]]
print(sum_of_evens(l))