def can_be_nested(list1, list2) -> bool:
    return min(list1)>min(list2) and max(list1)<max(list2)
print(can_be_nested([1,2,3,4],[0,6]))