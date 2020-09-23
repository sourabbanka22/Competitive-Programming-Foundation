def bubbleSort(array):
    # Write your code here.
    isSorted = False
    while not isSorted:
        isSorted = True
        for index in range(len(array)-1):
            if array[index]>array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                isSorted = False
    
    return array
