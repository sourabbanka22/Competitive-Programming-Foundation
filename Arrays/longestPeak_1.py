def longestPeak(array):
    # Write your code here.
    if len(array)==0:
        return 0
    
    left = [0 for val in array]
    right = [0 for val in array]
    result = [0 for val in array]

    for index in range(1, len(array)):
        if array[index] > array[index-1]:
            left[index] = left[index-1]+1
    
    for index in reversed(range(len(array)-1)):
        if array[index] > array[index+1]:
            right[index] = right[index+1]+1
    
    for index in range(len(array)):
        if left[index]==0 or right[index]==0:
            continue
        else:
            result[index] = left[index]+right[index] + 1
    
    return max(result)

print(longestPeak([1, 2, 3, 3, 2, 1]))
print(longestPeak([5, 4, 3, 2, 1, 2, 1]))