import string
def print_rangoli(size):
    alpha=string.ascii_lowercase
    n=size
    lines=[]
    for i in range(n):
        s='-'.join(alpha[n-1:i:-1]+alpha[i:n])
        lines.append(s.center(4*n-3,'-'))
    print('\n'.join(lines[::-1]+lines[1:]))
n=int(input())
print_rangoli(n)