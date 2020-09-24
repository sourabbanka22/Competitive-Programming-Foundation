def longestPeak(array):
    # Write your code here.
    result = 0

    for index in range(1, len(array)-1):
        left = index-1
        right = index+1
        currentMax = 0
        if array[index]>array[left] and array[index]>array[right]:
            while left >= 0 and array[left]>array[left-1]:
                left -= 1
            while right+1 < len(array) and array[right]>array[right+1]:
                right += 1
            currentMax = right-left+1
            if currentMax>result:
                result = currentMax

    return result

print(longestPeak([1, 2, 3, 3, 2, 1]))
print(longestPeak([5, 4, 3, 2, 1, 2, 1]))