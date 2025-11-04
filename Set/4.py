n = int(input())
english = set(map(int, input().split()))


b = int(input())
french = set(map(int, input().split()))

# students who subscribed to either english or french but not both newspaper
notboth_set = (english.union(french)).difference((english).intersection(french))

print(len(notboth_set))