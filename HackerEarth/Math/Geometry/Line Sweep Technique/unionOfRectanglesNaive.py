def getArea(width, openIntervals):

    area = 0
    previousY = float("-inf")
    for bottomY, topY in openIntervals:
        previousY = max(previousY, bottomY)
        area += max(0, (topY - previousY) * width)
        previousY = max(topY, previousY)
    
    return area

# Time Complexity: N^2log(N)
def unionOfRectangles(rectangles):
    
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append([x1, 0, y1, y2])
        events.append([x2, 1, y1, y2])
    events.sort()
    
    area = 0
    previousX = float("-inf")
    openIntervals = []
    for event in events:
        currentX, close, y1, y2 = event
        area += getArea(currentX - previousX, openIntervals)
        if close:
            openIntervals.remove((y1,y2))
        else:
            openIntervals.append((y1,y2))
            openIntervals.sort()
        previousX = currentX
    
    return area

numOfRectangles = int(input())
rectangles = []

for _ in range(numOfRectangles):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append([x1, y1, x2, y2])

# rectangles = [[2, 1, 4, 2], [2, 3, 4, 5], [1, 4, 3, 6]]
print(unionOfRectangles(rectangles))