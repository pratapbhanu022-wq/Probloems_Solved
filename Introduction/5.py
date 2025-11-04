# The provided code stub reads an integer,n, from STDIN. For all non-negative integers i<n print n**2
n = int(input('Enter number : '))
'''for i in range(n):
   print(i**2) # this is the main code
'''
for i in range(n):
    i+=1
    print(i**2)
    