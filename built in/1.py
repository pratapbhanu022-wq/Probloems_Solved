a,b=map(int,input().split())
lists=[]
for i in range(b):
    s=list(map(float,input().split()))
    lists.append(s)
zipped=zip(*lists)
for item in zipped:
    print(f"{sum(item)/len(item):.1f}")
