def insertionSort(array):
    # Write your code here.
    for rightIdx in range(1, len(array)):
        leftIdx = rightIdx
        while leftIdx>0 and array[leftIdx-1]>array[leftIdx]:
            array[leftIdx-1], array[leftIdx] = array[leftIdx], array[leftIdx-1]
            leftIdx -= 1
    return array
