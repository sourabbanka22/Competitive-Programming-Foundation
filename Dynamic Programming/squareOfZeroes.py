def squareOfZeroes(matrix):
    # Write your code here.
    infoMatrix = preComputeValues(matrix)
    size  = len(matrix)
    for topRow in range(size):
        for leftCol in range(size):
            squareLength = 2
            while squareLength<=size-leftCol and squareLength<=size-topRow:
                bottomRow = topRow+squareLength-1
                rightCol = leftCol+squareLength-1
                if isSquareOfZeroes(infoMatrix, topRow, leftCol, bottomRow, rightCol):
                    return True
                squareLength+=1
    return False

def isSquareOfZeroes(infoMatrix, r1, c1, r2, c2):
    squareLength = r2-r1+1
    hasTopBorder = infoMatrix[r1][c1]["numZeroesRight"] >= squareLength
    hasLeftBorder = infoMatrix[r1][c1]["numZeroesBelow"] >= squareLength
    hasBottomBorder = infoMatrix[r2][c1]["numZeroesRight"] >= squareLength
    hasRightBorder = infoMatrix[r1][c2]["numZeroesBelow"] >= squareLength

    return hasTopBorder and hasLeftBorder and hasBottomBorder and hasRightBorder

def preComputeValues(matrix):
    infoMatrix = [[None for _ in row] for row in matrix]
    size = len(matrix)

    for row in range(size):
        for col in range(size):
            numZeroes = 1 if matrix[row][col]==0 else 0
            infoMatrix[row][col] = {
                "numZeroesBelow": numZeroes,
                "numZeroesRight": numZeroes,
            }
    
    lastIdx = len(matrix)-1
    for row in reversed(range(size)):
        for col in reversed(range(size)):
            if matrix[row][col] == 1:
                continue
            if row<lastIdx:
                infoMatrix[row][col]["numZeroesBelow"] += infoMatrix[row+1][col]["numZeroesBelow"]
            if col<lastIdx:
                infoMatrix[row][col]["numZeroesRight"] += infoMatrix[row][col+1]["numZeroesRight"]

    return infoMatrix

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

# funMatrix = [[16, 15, 14, 13], 
#             [12, 11, 10, 9], 
#             [8, 7, 6, 5], 
#             [4, 3, 2, 1]]
# funList = []
# for row in reversed(range(len(funMatrix))):
#     for col in reversed(range(len(funMatrix[0]))):
#         funList.append(funMatrix[row][col])
# print(funList)

print(squareOfZeroes(matrix2))