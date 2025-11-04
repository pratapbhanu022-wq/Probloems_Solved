N, M= map(int,input().split())
for i in range(N//2):
    row = (".|." * (2*i+1)).center(M,"-")
    print(row)
print("WELCOME".center(M,"-"))
for i in range(N//2 -1,-1,-1):
    row = (".|."*(2*i+1)).center(M,"-")
    print(row)