# to find if A is subset of B
n=int(input('number of total commands : '))
for i in range(n):
    An = int(input('total eliment is set A : '))
    A = set(map(int,input().split()))
    Bn = int(input('total eliment is set B : '))
    B = set(map(int,input().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)
      
  
   
