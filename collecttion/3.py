'''
from collections import namedtuple
N = int(input())
STUDENT = namedtuple('STUDENTS', input())
total = 0
for i in range(N):
    obj = STUDENT(*input().split())
    total=total+int(obj.MARKS)
print(round(total/N,2))
'''
# in 4 lines
from collections import namedtuple
N,STUDENT = int(input()),namedtuple('STUDENTS', input())
total=sum ([ int(STUDENT(*input().split()).MARKS)  for i in range  (N)])
print(round(total/N,2))

