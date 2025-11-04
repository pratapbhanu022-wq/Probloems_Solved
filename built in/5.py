n=int(input())
l=list(map(int,input().split()))
if all(item>0 for item in l) and any(str(item)==str(item)[::-1] for item in l):
      print(True)
else:
      print(False)