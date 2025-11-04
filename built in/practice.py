s=input("")
l=list(s)
converted=[int(x) if x.isdigit() else x for x in l]
sorted_list=sorted(
    converted,
    key=lambda x:(0,x) if isinstance(x,int)and x%2==0 else(1,x) if isinstance(x,int) else (2, str(x)))
sorted_list=sorted(
    converted,
    key=lambda x:(0,x) if isinstance(x,int)and x%2==1 else(1,x) if isinstance(x,int) else (2, str(x)))

sorted_list=sorted(
    converted,
    key=lambda x:(0,x) if isinstance(x,str)and x.isupper() else(1,str(x)) if isinstance(x,str) else (2, x))
sorted_list=sorted(
    converted,
    key=lambda x:(0,x) if isinstance(x,str)and x.islower() else(1,str(x)) if isinstance(x,str) else (2, x))

c=[str(y) if isinstance(y,str) and y.isalpha() else str(y) for y in sorted_list]
p="".join(c)
print(p)