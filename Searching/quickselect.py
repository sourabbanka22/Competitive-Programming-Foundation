def quickselect(array, k):
    # Write your code here.
    position = k-1
    kth = quickselectUtil(array, 0, len(array)-1, position)
    return kth

def quickselectUtil(array, left, right, position):
    
    while True:
        pivot = left
        currentLeft = left+1
        currentRight = right

        while currentLeft <= currentRight:
            if array[currentLeft]>array[pivot] and array[pivot]>array[currentRight]:
                swap(array, currentLeft, currentRight)
            if array[currentLeft] <= array[pivot]:
                currentLeft += 1
            if array[currentRight] >= array[pivot]:
                currentRight -= 1
        swap(array, currentRight, pivot)

        if position == currentRight:
            return array[currentRight]
        elif position < currentRight:
            right = currentRight-1
        else:
            left = currentRight+1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# print(quickselect([3, 1, 7, 8, 0, 2, 12, 11], 4))
print(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 2))
print(quickselect([43, 24, 37], 1))