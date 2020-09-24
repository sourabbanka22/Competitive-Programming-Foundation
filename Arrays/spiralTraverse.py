def spiralTraverse(array):
    # Write your code here.
    leftExtreme = 0
    rightExtreme = len(array[0])-1
    topExtreme = 0
    bottomExtreme = len(array)-1

    spirallyTraversedArray = []

    while leftExtreme<=rightExtreme and topExtreme<=bottomExtreme:
        
        for col in range(leftExtreme, rightExtreme+1):
            spirallyTraversedArray.append(array[topExtreme][col])
        
        for row in range(topExtreme+1, bottomExtreme+1):
            spirallyTraversedArray.append(array[row][rightExtreme])
        
        for col in reversed(range(leftExtreme, rightExtreme)):
            if topExtreme == bottomExtreme:
                break
            spirallyTraversedArray.append(array[bottomExtreme][col])
        
        for row in reversed(range(topExtreme+1, bottomExtreme)):
            if leftExtreme == rightExtreme:
                break
            spirallyTraversedArray.append(array[row][leftExtreme])
        
        topExtreme += 1
        rightExtreme -= 1
        bottomExtreme -= 1
        leftExtreme += 1

    return spirallyTraversedArray

matrix1 = [[1, 2, 3, 4], 
        [12, 13, 14, 5], 
        [11, 16, 15, 6], 
        [10, 9, 8, 7]]
print(spiralTraverse(matrix1))

matrix2 = [[1, 2, 3, 4], 
        [10, 11, 12, 5], 
        [9, 8, 7, 6]]
print(spiralTraverse(matrix2))
        