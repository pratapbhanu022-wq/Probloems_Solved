# Convert Matrix to Dictionary of Row Sums
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_sum={f"row_{i+1} ": sum(row) for i,row in enumerate(matrix)}
print(row_sum) # {'row_1 ': 6, 'row_2 ': 15, 'row_3 ': 24}