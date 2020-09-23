def searchForRange(array, target):
    # Write your code here.
    left = getIndex(array, target, True)
    right = getIndex(array, target, False)

    return [left, right]


def getIndex(array, target, goLeft):
    leftIdx = 0
    rightIdx = len(array)-1
    
    while leftIdx <= rightIdx:
        midIdx = (leftIdx+rightIdx)//2
        if target == array[midIdx]:
            if goLeft:
                if midIdx == 0:
                    return midIdx
                else:
                    if array[midIdx-1] != target:
                        return midIdx
                    else:
                        rightIdx = midIdx-1
            else:
                if midIdx == len(array)-1:
                    return midIdx
                else:
                    if array[midIdx+1] != target:
                        return midIdx
                    else:
                        leftIdx = midIdx+1
        elif target>array[midIdx]:
            leftIdx = midIdx+1
        else:
            rightIdx = midIdx-1
    return -1

print(searchForRange([5, 7, 7, 8, 8, 10], 7))
