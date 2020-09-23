def quickSort(array):
    # Write your code here.
    quickSortUtil(array, 0, len(array)-1)
    return array

def quickSortUtil(array, left, right):
    if left>=right:
        return
    
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
    
    quickSortUtil(array, left, currentRight-1)
    quickSortUtil(array, currentRight+1, right)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print(quickSort([3, 1, 7, 8, 0, 2, 12, 11]))