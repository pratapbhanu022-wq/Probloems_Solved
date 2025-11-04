s_data = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        s_data.append([name,score])
        
print(s_data)
scores = sorted(set([s[1] for s in s_data]))
second_lowest = scores [1]
result = [s[0] for s in s_data if s[1]==second_lowest]
result.sort()
for name in result:
        print(name)