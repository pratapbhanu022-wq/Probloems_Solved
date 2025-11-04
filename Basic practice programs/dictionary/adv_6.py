# grading system
students = {'Alice': 85, 'Bob': 67, 'Charlie': 91, 'David': 74, 'Eve': 58}
grades = {'A': [], 'B': [], 'C': [], 'D': [], 'F': []}

for name, marks in students.items():
    if marks >= 90:
        grades['A'].append(name)
    elif marks >= 80:
        grades['B'].append(name)
    elif marks >= 70:
        grades['C'].append(name)
    elif marks >= 60:
        grades['D'].append(name)
    else:
        grades['F'].append(name)

print(grades)