import numpy

N, M = list(map(int, input().split()))

array_lst =[]

for _ in range(N):
    inp = input().split()
    lst = [int(inp[i]) for i in range(M)]
    array_lst.append(lst)
    
np_array = numpy.array(array_lst)
max_array= numpy.min(np_array, axis= 1)
print(numpy.max((max_array)))