def productExceptSelf(nums):
    n = len(nums)
    res = [1]*n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res
print(productExceptSelf([10,3,5,6,2]))
# Example: [10, 3, 5, 6, 2] → [180, 600, 360, 300, 900]