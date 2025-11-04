# working with sets to get the output
# Number of students who subscribed to both
n = int(input())
english = set(map(int, input().split()))

# Number of students who subscribed to French
b = int(input())
french = set(map(int, input().split()))

# intersection of both sets (students who subscribed to both newspaper)
inter_set = english.intersection(french)

print(len(inter_set))
