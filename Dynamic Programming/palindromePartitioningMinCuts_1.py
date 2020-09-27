def palindromePartitioningMinCuts(string):
    # Write your code here.
    minCutsString = minCuts(string)
    minCutsWithReversedString = minCuts(string[::-1])

    return minCutsString if minCutsString<minCutsWithReversedString else minCutsWithReversedString


def minCuts(string):
    cuts = 0
    left, right = 0, len(string)
    while left<right:
        currentMax = 0
        innerLeft, innerRight, currentRight = left, left, left
        currentList = []
        while innerRight<len(string):
            currentList.append(string[innerRight])
            if currentList==currentList[::-1] and len(currentList)>currentMax:
                currentMax = len(currentList)
                currentRight = innerRight
            innerRight += 1
        # print(string[left:currentRight+1])
        cuts += 1
        left = currentRight+1
    
    return cuts-1


print(palindromePartitioningMinCuts("noonabbad"))
print(palindromePartitioningMinCuts("ababbbabbababa"))