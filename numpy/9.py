import numpy

array_list =[]
N, M = map(int, input().split())
for _ in range(N):
    arr= list(map(int, input().split()))
    array_list.append(arr)
    
numpy_array= numpy.array(array_list)
np_sum= numpy.sum(numpy_array, axis= 0)
np_product_of_sum= numpy.prod(np_sum)

print(np_product_of_sum)