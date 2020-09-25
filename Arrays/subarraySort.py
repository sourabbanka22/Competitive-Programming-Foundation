def subarraySort(array):
    # Write your code here.
    
    smallestOutOfOrder = float("inf")
    largestOutOfOrder = float("-inf")
    for leftIdx in range(1, len(array)):
        if array[leftIdx] < array[leftIdx-1] and smallestOutOfOrder>array[leftIdx]:
            smallestOutOfOrder = array[leftIdx]
    for rightIdx in reversed(range(len(array)-1)):
        if array[rightIdx] > array[rightIdx+1] and largestOutOfOrder<array[rightIdx]:
            largestOutOfOrder = array[rightIdx]
    
    if smallestOutOfOrder == float("inf"):
        return [-1, -1]
    
    left = 0
    while smallestOutOfOrder>=array[left]:
        left += 1
    right = len(array)-1
    while largestOutOfOrder <= array[right]:
        right-=1
    
    return [left, right]

print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
print(subarraySort([2, 1]))