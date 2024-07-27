def setZeroes(matrix):
    rows = []
    columns = []

    for i in range(len(matrix)):
        if 0 in matrix[i]:
            rows.append(i)
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                columns.append(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in columns:
                matrix[i][j] = 0

    return matrix    

# Example 1:
# Input: 
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: 
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
