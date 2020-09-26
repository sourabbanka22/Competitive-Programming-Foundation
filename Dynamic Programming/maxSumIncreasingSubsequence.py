def maxSumIncreasingSubsequence(array):
    # Write your code here.
    summation = [val for val in array]
    prevIdx = [None for _ in array]
    
    for index in range(1, len(array)):
        currentMax = 0
        for left in range(0, index):
            if currentMax<summation[left] and array[left]<array[index]:
                currentMax = summation[left]
                prevIdx[index] = left
        summation[index] += currentMax
    
    finalArray = []
    maxIdx = summation.index(max(summation))
    while maxIdx is not None:
        finalArray.append(array[maxIdx])
        maxIdx = prevIdx[maxIdx]
    
    return [max(summation), finalArray[::-1]]

print(maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7]))
print(maxSumIncreasingSubsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))
print(maxSumIncreasingSubsequence([-1, 1]))