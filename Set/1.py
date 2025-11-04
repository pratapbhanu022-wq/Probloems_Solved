# working with union to get the output
# Number of students who subscribed to English
n = int(input())
english = set(map(int, input().split()))

# Number of students who subscribed to French
b = int(input())
french = set(map(int, input().split()))

# Union of both sets (students who subscribed to at least one newspaper)
union_set = english.union(french)

print(len(union_set))
