def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array)-1
    while left<right:
        if array[left] != toMove:
            left += 1
        if array[right] == toMove:
            right -= 1
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]

    return array

print(moveElementToEnd([2, 4, 5, 6, 2, 10], 2))