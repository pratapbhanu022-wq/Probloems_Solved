from collections import Counter
x =int(input())
shoe_size = list(map(int,input().split()))
shoe_count=Counter(shoe_size)
N = int(input())
income=0

for i in range(N):
   size, price= map(int,input().split())
   if shoe_count[size]>0:
      income+=price
      shoe_count[size]-=1
print(income)