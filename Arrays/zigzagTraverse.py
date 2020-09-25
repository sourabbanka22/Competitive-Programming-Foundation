def zigzagTraverse(array):
    # Write your code here.
    leftExtreme = 0
    topExtreme = 0
    rightExtreme = len(array[0])-1
    bottomExtreme = len(array)-1

    row, col = 0, 0
    goingDown = True
    zigZagArray = []
    
    while row<=bottomExtreme and col<=rightExtreme:
        zigZagArray.append(array[row][col])
        if goingDown:
            if col == leftExtreme or row == bottomExtreme:
                goingDown = False
                if row == bottomExtreme:
                    col += 1
                elif col == leftExtreme:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == topExtreme or col == rightExtreme:
                goingDown = True
                if col == rightExtreme:
                    row += 1
                elif row == topExtreme:
                    col += 1
            else:
                row -= 1
                col += 1
            
    return zigZagArray


matrix = [[1, 3, 4, 10], 
          [2, 5, 9, 11], 
          [6, 8, 12, 15], 
          [7, 13, 14, 16]]
print(zigzagTraverse(matrix))