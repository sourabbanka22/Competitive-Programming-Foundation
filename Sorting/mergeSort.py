def mergeSort(array):
    # Write your code here.
    sortedArray = array[:]
    mergeSortUtil(array, 0, len(array)-1, sortedArray, 0)
    return sortedArray

def mergeSortUtil(array, left, right, sortedArray, index):
    if left == right:
        return
    mid = (left+right)//2
    mergeSortUtil(sortedArray, left, mid, array, index+1)
    mergeSortUtil(sortedArray, mid+1, right, array, index+1)
    merge(array, left, mid, right, sortedArray)

def merge(array, left, mid, right, sortedArray):
    leftStart = left
    rightStart = mid+1
    newIdx = left
    while leftStart<=mid and rightStart<=right:
        if array[leftStart] <= array[rightStart]:
            sortedArray[newIdx] = array[leftStart]
            leftStart += 1
        else:
            sortedArray[newIdx] = array[rightStart]
            rightStart += 1
        newIdx += 1
    while leftStart <= mid:
        sortedArray[newIdx] = array[leftStart]
        leftStart += 1
        newIdx += 1
    while rightStart <= right:
        sortedArray[newIdx] = array[rightStart]
        rightStart += 1
        newIdx += 1

print(mergeSort([12, 11, 10, 9, 8, 7, 6, 5]))