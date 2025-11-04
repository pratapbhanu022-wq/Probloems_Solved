# Matrix Diagonals from Tuple
matrix = ((1,2,3), (4,5,6), (7,8,9))
n = len(matrix)
primary = tuple(matrix[i][i] for i in range(n))
secondary = tuple(matrix[i][n-i-1] for i in range(n))
print(primary, secondary) # (1, 5, 9) (3, 5, 7)
