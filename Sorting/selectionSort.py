def selectionSort(array):
    # Write your code here.
    for index in range(len(array)):
        currentIdx = index
        minimum = float("inf")
        minIdx = 0
        while currentIdx<len(array)-1:
            if minimum>array[currentIdx]:
                minimum = array[currentIdx]
                minIdx = currentIdx
            currentIdx += 1
        array[index], array[minIdx] = array[minIdx], array[index]
    
    return array