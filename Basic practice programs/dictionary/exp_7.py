# Find All Pairs with Same Sum Using Dictionary
nums = [1, 2, 3, 4, 5, 6]
pairs = {}
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        s = nums[i] + nums[j]
        pairs.setdefault(s, []).append((nums[i], nums[j]))
print(pairs)
'''
{3: [(1, 2)], 4: [(1, 3)], 5: [(1, 4), (2, 3)], 6: [(1, 5), (2, 4)],
 7: [(1, 6), (2, 5), (3, 4)], 8: [(2, 6), (3, 5)], 
 9: [(3, 6), (4, 5)], 10: [(4, 6)], 11: [(5, 6)]}
'''