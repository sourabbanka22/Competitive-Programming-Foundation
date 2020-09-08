# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        startIdx = (len(array) - 2)//2
        for index in reversed(range(startIdx+1)):
            self.siftDown(index, len(array) - 1, array) 
        return array

    def siftDown(self, startIdx, endIdx, array):
        # Write your code here.
        firstChild = startIdx*2 + 1
        
        while firstChild <= endIdx:
            secondfChild = startIdx*2 + 2 if startIdx*2 + 2 < len(array) else -1
            if secondfChild != -1 and array[firstChild]["element"] > array[secondfChild]["element"]:
                swapIndex = secondfChild
            else:
                swapIndex = firstChild
            if array[swapIndex]["element"] < array[startIdx]["element"]:
				self.swap(startIdx, swapIndex, array)
                startIdx = swapIndex
                firstChild = startIdx*2 + 1
            else:
                break
            

    def siftUp(self, index):
        # Write your code here.
        parnetIdx = (index-1)//2
        while index>0 and self.heap[index]["element"] < self.heap[parnetIdx]["element"]:
            self.swap(index, parnetIdx, self.heap)
            index = parnetIdx
            parnetIdx = (index-1)//2


    def peek(self):
        # Write your code here.
        return self.heap[0]["element"]

    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap)-1, self.heap)
        last = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return last

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)

    def swap(self, first, second, array):
        array[first], array[second] = array[second], array[first]
    
    def isEmpty(self):
        return len(self.heap) == 0

    def returnHeap(self):
        return self.heap

def mergeSortedArrays(arrays):

    arrayOfDict = []
    sortedSingleArray = []

    for arrayNum in range(len(arrays)):
        arrayOfDict.append({"arrayNum": arrayNum, "elementIdx": 0, "element": arrays[arrayNum][0]})
    
    minHeap = MinHeap(arrayOfDict)

    while not minHeap.isEmpty():
        valueToAdd = minHeap.remove()
        elementIdx, arrayNum, element = valueToAdd["elementIdx"], valueToAdd["arrayNum"], valueToAdd["element"]
        sortedSingleArray.append(element)
        if len(arrays[arrayNum])-1 == elementIdx:
            continue
        minHeap.insert({"arrayNum": arrayNum, "elementIdx": elementIdx+1, "element": arrays[arrayNum][elementIdx+1]})

    return sortedSingleArray

arrays = [[1, 2, 3, 4, 5], [8, 9], [6, 7, 23, 47, 81], [-1, 3, 124, 160]]

print(mergeSortedArrays(arrays))