def getArea(width, openIntervals):
    
    sortedIntervals = openIntervals.inOrder()
    if sortedIntervals[0] is None:
        return 0
    
    area = 0
    previousY = float("-inf")
    for bottomY, topY in sortedIntervals:
        previousY = max(previousY, bottomY)
        area += max(0, (topY - previousY) * width)
        previousY = max(topY, previousY)

    return area

# Time Complexity: N^2
def unionOfRectangles(rectangles):

    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append([x1, 0, y1, y2])
        events.append([x2, 1, y1, y2])
    events.sort()

    area = 0
    previousX = float("-inf")
    openIntervals = None
    first = True
    
    for event in events:
        currentX, close, y1, y2 = event
        if not first:
            area += getArea(currentX - previousX, openIntervals)
        if close:
            openIntervals.remove([y1,y2])
        else:
            if first:
                openIntervals = BST([y1,y2])
                first = False
            else:
                openIntervals.insert([y1,y2])
        
        previousX = currentX

    return area

class BST:
    def __init__(self, pair):
        self.value = pair[0]
        self.pair = pair
        self.left = None
        self.right = None

    def insert(self, pair):
        currentNode = self
        value = pair[0]
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(pair)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(pair)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def remove(self, pair, parentNode=None):
        currentNode = self
        value = pair[0]
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    minValuePair = currentNode.right.getMinValuePair()
                    currentNode.value, currentNode.pair = minValuePair[0], minValuePair
                    currentNode.right.remove(currentNode.pair, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.pair = currentNode.left.pair
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.pair = currentNode.right.pair
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                        currentNode.pair = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValuePair(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.pair

    def inOrder(self):
        return self.inOrderUtil([])

    def inOrderUtil(self, array):
        if self is None:
            return
        if self.left is not None:
            self.left.inOrderUtil(array)
        array.append(self.pair)
        if self.right is not None:
            self.right.inOrderUtil(array)

        return array


numOfRectangles = int(input())
rectangles = []

for _ in range(numOfRectangles):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append([x1, y1, x2, y2])

# rectangles = [[2, 1, 4, 2], [2, 3, 4, 5], [1, 4, 3, 6]]

print(unionOfRectangles(rectangles))