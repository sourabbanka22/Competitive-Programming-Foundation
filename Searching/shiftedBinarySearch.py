def shiftedBinarySearch(array, target):
    # Write your code here.
    leftIdx = 0
    rightIdx = len(array)-1
    
    while leftIdx <= rightIdx:
        midIdx = (leftIdx+rightIdx)//2
        print(array[leftIdx], array[midIdx], array[rightIdx])
        if target == array[midIdx]:
            return midIdx
        elif array[leftIdx]<=array[midIdx]:
            if target>=array[leftIdx] and target<array[midIdx]:
                rightIdx = midIdx-1
            else:
                leftIdx = midIdx+1
        else:
            if target>array[midIdx] and target<=array[rightIdx]:
                leftIdx = midIdx+1
            else:
                rightIdx = midIdx-1
    return -1

print(shiftedBinarySearch([71, 72, 73, 0, 1, 21, 33, 37, 45, 61], 73))
print(shiftedBinarySearch([71, 72, 73, 85, 97, 99, 109, 0, 1, 21, 33, 37, 45, 61], 73))

# if target>array[leftIdx] and target<array[midIdx]:
#     rightIdx = midIdx-1
# else:
#     leftIdx = midIdx+1