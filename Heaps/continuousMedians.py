# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.minHeap = MinHeap([])
        self.maxHeap = MaxHeap([])
        self.median = None

    def insert(self, number):
        # Write your code here.
        
        if self.maxHeap.isEmpty():
            self.maxHeap.insert(number)
        elif number < self.maxHeap.peek(): 
            self.maxHeap.insert(number)
        else: 
            self.minHeap.insert(number)

        minLen = len(self.minHeap.returnHeap())
        maxLen = len(self.maxHeap.returnHeap())
        if minLen - maxLen == 2:
            poppedValue = self.minHeap.remove()
            self.maxHeap.insert(poppedValue)
        elif minLen - maxLen == -2:
            poppedValue = self.maxHeap.remove()
            self.minHeap.insert(poppedValue)

        median = 0
        minLen = len(self.minHeap.returnHeap())
        maxLen = len(self.maxHeap.returnHeap())
        if (minLen + maxLen) % 2 == 0:
            median = (self.minHeap.peek() + self.maxHeap.peek()) / 2
        elif minLen > maxLen:
            median = self.minHeap.peek()
        else:
            median = self.maxHeap.peek()

        self.median = median

    def getMedian(self):
        return self.median

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
                self.swap(startIdx, swapIndex, array)
                startIdx = swapIndex
                firstChild = startIdx*2 + 1
            else:
                break  

    def siftUp(self, index):
        # Write your code here.
        parnetIdx = (index-1)//2
        while index>0 and self.heap[index] < self.heap[parnetIdx]:
            self.swap(index, parnetIdx, self.heap)
            index = parnetIdx
            parnetIdx = (index-1)//2

    def peek(self):
        # Write your code here.
        return self.heap[0]

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

class MaxHeap:
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
            if secondfChild != -1 and array[firstChild] < array[secondfChild]:
                swapIndex = secondfChild
            else:
                swapIndex = firstChild
            if array[swapIndex] > array[startIdx]:
                self.swap(startIdx, swapIndex, array)
                startIdx = swapIndex
                firstChild = startIdx*2 + 1
            else:
                break

    def siftUp(self, index):
        # Write your code here.
        parnetIdx = (index-1)//2
        while index>0 and self.heap[index] > self.heap[parnetIdx]:
            self.swap(index, parnetIdx, self.heap)
            index = parnetIdx
            parnetIdx = (index-1)//2

    def peek(self):
        # Write your code here.
        return self.heap[0]

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

cMH = ContinuousMedianHandler()
cMH.insert(5)
print(cMH.getMedian())
cMH.insert(10)
print(cMH.getMedian())
cMH.insert(100)
print(cMH.getMedian())