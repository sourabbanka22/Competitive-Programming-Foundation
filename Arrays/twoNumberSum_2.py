def twoNumberSum(array, targetSum):
    array.sort()
    front = 0
    back = len(array)-1
    result = []
    while front < back:
        if array[front] + array[back] == targetSum:
            result.append(array[front])
            result.append(array[back])
            return result
        elif array[front] + array[back] > targetSum:
            back -= 1
        else:
            front += 1
    return result