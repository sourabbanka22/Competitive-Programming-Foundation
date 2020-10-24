import math

def convertToString(point):
    return str(point[0])+" "+str(point[1])

def convertToPoint(string):
    a, b = map(int, string.split(" "))
    return [a, b]

def findDistance(point1, point2):
    yDist = (point2[1]-point1[1])*(point2[1]-point1[1])
    xDist = (point2[0]-point1[0])*(point2[0]-point1[0])
    return math.sqrt(xDist+yDist)

def closestPair(points):
    n = len(points)

    points.sort(key = lambda x:x[0])
    best = float("inf")
    box = set()
    box.add(convertToString(points[0]))
    
    for idx in range(1, n):
        
        toRemove = []
        toAdd = []
        for pointString in box:
            point = convertToPoint(pointString)
            distance = findDistance(point, points[idx])
            if distance<best:
                best = distance
                toAdd.append(pointString)
            else:
                toRemove.append(pointString)
        
        for val in toRemove:
            box.remove(val)
        
        for val in toAdd:
            box.add(val)
    
    return best

points = [[0, 5], [5, 1], [2, 3], [4, 2]]
print(closestPair(points))