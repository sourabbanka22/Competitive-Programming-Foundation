def fourNumberSum(array, targetSum):
    # Write your code here.
    memo = {}
    result = []
    for firstIdx in range(len(array)):
        
        for secondIdx in range(firstIdx+1, len(array)):
            currentSum = array[firstIdx]+array[secondIdx]
            subtractedSum = targetSum-currentSum
            if subtractedSum in memo:
                for pair in memo[subtractedSum]:
                    result.append(pair+[array[firstIdx], array[secondIdx]])
        
        for thirdIdx in range(0, firstIdx):
            currentSum = array[firstIdx]+array[thirdIdx]
            if currentSum not in memo:
                memo[currentSum] = [[array[thirdIdx], array[firstIdx]]]
            else:
                memo[currentSum].append([array[thirdIdx], array[firstIdx]])

    return result


print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))