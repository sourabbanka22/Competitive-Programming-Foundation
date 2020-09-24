def heapSort(array):
    # Write your code here.
    buildHeap(array)
    for lastIdx in reversed(range(1, len(array))):
        swap(0, lastIdx, array)
        siftDown(0, lastIdx-1, array)
    return array


def buildHeap(array):
    startIdx = (len(array) - 2)//2
    for index in reversed(range(startIdx+1)):
        siftDown(index, len(array) - 1, array)

def siftDown(startIdx, endIdx, array):
    firstChild = startIdx*2 + 1
    
    while firstChild <= endIdx:
        secondChild = startIdx*2 + 2 if startIdx*2 + 2 <= endIdx else -1
        if secondChild > -1 and array[firstChild] < array[secondChild]:
            swapIndex = secondChild
        else:
            swapIndex = firstChild
        if array[swapIndex] > array[startIdx]:
            swap(startIdx, swapIndex, array)
            startIdx = swapIndex
            firstChild = startIdx*2 + 1
        else:
            break

def swap(first, second, array):
    array[first], array[second] = array[second], array[first]


print(heapSort([1, 2, 3]))