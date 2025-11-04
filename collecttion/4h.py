from collections import OrderedDict
n=int(input())
ordered_dict = OrderedDict()
for i in range(n):
    item,price=input().rsplit(" ",1) # split from right item name may contain space
    price = int(price)
    if item in ordered_dict:
        ordered_dict[item]+=price
    else:
        ordered_dict[item]=price
for k,v in ordered_dict.items():
    print(k,v)