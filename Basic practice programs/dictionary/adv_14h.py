# Nested dictionary – Find student with highest average
students = {
    'Alice': {'math': 88, 'science': 90, 'english': 75},
    'Bob': {'math': 70, 'science': 65, 'english': 80},
    'Charlie': {'math': 95, 'science': 85, 'english': 100}
}

averages = {name: sum(marks.values()) / len(marks) for name, marks in students.items()}
top_student = max(averages, key=averages.get)

print(f"Top Student: {top_student} with Average: {averages[top_student]}")
