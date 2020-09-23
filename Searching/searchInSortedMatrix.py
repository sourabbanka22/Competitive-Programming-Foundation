def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row = 0
    col = len(matrix[0])-1
    
    while row>=0 and col>=0 and row<len(matrix) and col<len(matrix[0]):
        print(row, col)
        if target == matrix[row][col]:
            return [row, col]
        elif target > matrix[row][col]:
            row += 1
        else:
            col -= 1
    
    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]
print(searchInSortedMatrix(matrix, 35))