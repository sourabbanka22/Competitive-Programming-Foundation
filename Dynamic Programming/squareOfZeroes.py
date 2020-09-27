def squareOfZeroes(matrix):
    # Write your code here.
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for lowestRow in range(row+1, len(matrix)):
                for rightMostCol in range(col+1, len(matrix[0])):
                    innerRow = row
                    innerCol = col+1
                    print(innerRow, lowestRow, innerCol, rightMostCol)
                    if matrix[row][col]==1:
                        continue
                    while innerRow<=lowestRow and innerCol<=rightMostCol:
                        print("Inside: ", innerRow, innerCol)
                        if innerRow==row and innerCol==col:
                            print("Its ME", innerRow, innerCol)
                            return True
                        
                        if matrix[innerRow][innerCol]==1:
                            break
                        elif innerCol == col:
                            innerRow -= 1
                        elif innerRow == lowestRow:
                            innerCol -= 1
                        elif innerCol == rightMostCol:
                            innerRow += 1
                        elif innerRow == row:
                            innerCol += 1
    return False

matrix1 = [[1, 1, 0, 1], 
            [1, 0, 0, 1], 
            [0, 0, 0, 1], 
            [1, 1, 1, 1]]

matrix2 = [
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1]
  ]

print(squareOfZeroes(matrix2))