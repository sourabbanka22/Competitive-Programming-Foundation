def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    memo = array[:]

    for index in range(2, len(array)):
        if index-3<0:
            memo[index] += memo[index-2]
        elif memo[index-2]>memo[index-3]:
            memo[index] += memo[index-2]
        else:
            memo[index] += memo[index-3]

    return max(memo)

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))