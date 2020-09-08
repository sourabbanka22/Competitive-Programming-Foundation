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
            if secondfChild != -1 and array[firstChild] > array[secondfChild]:
                swapIndex = secondfChild
            else:
                swapIndex = firstChild
            if array[swapIndex] < array[startIdx]:
                array[startIdx], array[swapIndex] = array[swapIndex], array[startIdx]
                startIdx = swapIndex
                firstChild = startIdx*2 + 1
            else:
                break
            

    def siftUp(self, index):
        # Write your code here.
        parnetIdx = (index-1)//2
        while index>0 and self.heap[index] < self.heap[parnetIdx]:
            self.swap(index, parnetIdx)
            index = parnetIdx
            parnetIdx = (index-1)//2


    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap)-1)
        last = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return last

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)
 
    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]
    
    def returnHeap(self):
        return self.heap

minHeap = MinHeap([5, 7, 6, 3, 4, 1, 11])
print(minHeap.returnHeap())
print(minHeap.remove())
print(minHeap.returnHeap())
print(minHeap.insert(-1))
print(minHeap.returnHeap())