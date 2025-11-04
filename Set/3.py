# working with sets to get the output
# Number of students who subscribed to English
n = int(input())
english = set(map(int, input().split()))

# Number of students who subscribed to French
b = int(input())
french = set(map(int, input().split()))

# difference of both sets (students who subscribed to english newspaper)
diff_set = english.difference(french)

print(len(diff_set))
