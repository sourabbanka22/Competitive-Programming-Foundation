def kadanesAlgorithm(array):
    # Write your code here.
    if len(array)==1:
        return array[0]
    
    for index in range(1, len(array)):
        array[index] = max(array[index], array[index-1]+array[index])

    return max(array)

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))