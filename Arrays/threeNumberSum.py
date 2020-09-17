def threeNumberSum(array, targetSum):
    # Write your code here.
    result = []
    array.sort()
    length = len(array)
    for grandParentIdx in range(length):
        parentIdx = grandParentIdx+1
        childIdx = length-1
        while parentIdx < childIdx:
            summation = array[grandParentIdx] + array[parentIdx] + array[childIdx]
            if summation == targetSum:
                result.append([array[grandParentIdx], array[parentIdx], array[childIdx]])
                parentIdx += 1
                childIdx -= 1
            elif summation < targetSum:
                parentIdx += 1
            else:
                childIdx -= 1
    
    return result