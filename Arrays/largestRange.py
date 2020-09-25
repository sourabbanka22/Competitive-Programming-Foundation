def largestRange(array):
    # Write your code here.
    memo = {}
    maxRange = float("-inf")
    finalRange = []

    for val in array:
        if val not in memo:
            memo[val] = False
    
    for val in array:
        if not memo[val]:
            currentRange = 1
            left = val-1
            right = val+1
            while left in memo and not memo[left]:
                memo[left] = True
                currentRange += 1
                left -= 1
            while right in memo and not memo[right]:
                memo[right] = True
                currentRange += 1
                right += 1
            if currentRange>maxRange:
                maxRange = currentRange
                finalRange = [left+1, right-1]

    return finalRange

print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
