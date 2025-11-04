''' Given the participants' score sheet for your University Sports Day,
 you are required to find the runner-up score. You are given n scores.
   Store them in a list and find the score of the runner-up.
'''
n = int(input())                     # number of scores
arr = list(map(int, input().split()))  # list of scores
# Convert to set to remove duplicates, then back to sorted list
unique_scores = sorted(set(arr))

# Second last element will be the runner-up
print(unique_scores[-2])
