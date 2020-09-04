def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if len(arrayOne) != len(arrayTwo) or arrayOne[0] != arrayTwo[0]:
        return False

    treeOneLeft = []
    treeTwoLeft = []
    for index in range(1, len(arrayOne)):
        if arrayOne[index] < arrayOne[0]:
            treeOneLeft.append(arrayOne[index])
        else:
            treeTwoLeft.append(arrayOne[index])

    treeOneRight = []
    treeTwoRight = []
    for index in range(1, len(arrayTwo)):
        if arrayTwo[index] < arrayTwo[0]:
            treeOneRight.append(arrayTwo[index])
        else:
            treeTwoRight.append(arrayTwo[index])

    return sameBsts(treeOneLeft, treeOneRight) and sameBsts(treeTwoLeft, treeTwoRight)

print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 10], [10, 8, 5, 15, 2, 10, 12, 94, 81]))