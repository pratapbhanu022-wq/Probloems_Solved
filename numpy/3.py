import numpy 

n_m = list(map(int, input().split()))
N = n_m[0]
M = n_m[1]

my_array = []
for _ in range(N):
    my_array.append(list(map(int, input().split())))

my_numpy_array = numpy.array(my_array)

print(numpy.transpose(my_numpy_array))
print(my_numpy_array.flatten())