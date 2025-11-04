# Find Key with Highest Average in Nested Dictionary
data = {
    'A': [10, 20, 30],
    'B': [25, 30, 35],
    'C': [5, 10, 15, 20]
}
avg = {k: sum(v)/len(v) for k, v in data.items()}
best = max(avg, key=avg.get)
print(f"{best} has highest avg: {avg[best]:.2f}")
# B has highest avg: 30.00
