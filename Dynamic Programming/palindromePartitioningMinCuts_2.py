def palindromePartitioningMinCuts(string):
    # Write your code here.
    isPallindrome = [[False for _ in string] for _ in string]
    
    for index in range(len(string)):
        isPallindrome[index][index] = True
    for length in range(2, len(string)+1):
        for leftIdx in range(len(string)-length+1):
            rightIdx = leftIdx+length-1
            if length==2:
                isPallindrome[leftIdx][rightIdx] = string[leftIdx]==string[rightIdx]
            else:
                isPallindrome[leftIdx][rightIdx] = string[leftIdx]==string[rightIdx] and isPallindrome[leftIdx+1][rightIdx-1]
    
    minCuts = [float("inf") for _ in string]

    for index in range(len(string)):
        if isPallindrome[0][index]:
            minCuts[index] = 0
        else:
            minCuts[index] = minCuts[index-1]+1
            for leftIdx in range(1, index):
                if isPallindrome[leftIdx][index] and minCuts[leftIdx-1]+1<minCuts[index]:
                    minCuts[index] = minCuts[leftIdx-1]+1
    return minCuts[-1]

# print(palindromePartitioningMinCuts("ooaba"))
print(palindromePartitioningMinCuts("noonabbad"))
print(palindromePartitioningMinCuts("ababbbabbababa"))