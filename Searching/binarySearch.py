def binarySearch(array, target):
    # Write your code here.
    leftIdx = 0
    rightIdx = len(array)-1
    
    while leftIdx <= rightIdx:
        midIdx = (leftIdx+rightIdx)//2
        print(array[midIdx])
        if target == array[midIdx]:
            return midIdx
        elif target>array[midIdx]:
            leftIdx = midIdx+1
        else:
            rightIdx = midIdx-1
    return -1

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))