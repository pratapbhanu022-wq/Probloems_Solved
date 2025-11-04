cube = lambda x: x**3
def fibonacci(n):
    s=[]
    a,b=0,1
    for i in range(n):
        s.append(a)
        a,b=b,a+b
    return s
n = int(input())
print(list(map(cube, fibonacci(n))))