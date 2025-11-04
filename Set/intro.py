def average(array):
    
    s=set(array)
    length = len(s)
    result=sum(s)/length
    return result

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)