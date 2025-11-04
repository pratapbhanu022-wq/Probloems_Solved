# Sort Tuple List by Multiple Rules
# Sort (name, age, salary) tuples by salary ↓, age ↑, then name
employees = [("Alice", 25, 80000), ("Bob", 22, 90000), ("Eve", 22, 90000)]
sorted_emp = sorted(employees, key=lambda x: (-x[2], x[1], x[0]))
print(sorted_emp)
# [('Bob', 22, 90000), ('Eve', 22, 90000), ('Alice', 25, 80000)]
