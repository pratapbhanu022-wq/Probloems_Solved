from collections import OrderedDict
n=int(input())
ordered_dict= OrderedDict()
for i in range(n):
    word = input()
    if word in ordered_dict:
        ordered_dict[word]=ordered_dict[word]+1
    else:
        ordered_dict[word]=1
print(len(ordered_dict))
result = " ".join(str(ordered_dict[key]) for key in ordered_dict)
print(result)
    