import math

def convertToString(point):
    return str(point[0])+" "+str(point[1])

def convertToPoint(string):
    a, b = map(float, string.split(" "))
    return [a, b]

def findDistance(point1, point2):
    yDist = (point2[1]-point1[1])*(point2[1]-point1[1])
    xDist = (point2[0]-point1[0])*(point2[0]-point1[0])
    return math.sqrt(xDist+yDist)

def closestPair(points):
    n = len(points)

    bestPair = []
    points.sort(key = lambda x:x[0])
    best = float("inf")
    box = set()
    box.add(convertToString(points[0]))
    
    for idx in range(1, n):

        toRemove = []
        for pointString in box:
            point = convertToPoint(pointString)
            if point[0]>=points[idx][0]-best and (point[1]>=points[idx][1]-best or point[1]<=points[idx][1]+best):
                continue
            toRemove.append(pointString)
        
        for pnt in toRemove:
            box.discard(pnt)
        
        for pointString in box:
            point = convertToPoint(pointString)
            currentDistance = findDistance(point, points[idx])
            if currentDistance<best:
                best = currentDistance
                bestPair = [point, points[idx]]
        box.add(convertToString(points[idx]))
            
    return (best, bestPair)

points = [[0, 5], [5, 1], [2, 3], [4, 2]]
points2 = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
points3 = [[1, 496.5], [12,30], [40, 50], [5, 1], [12, 10], [3,4], [1, 496], [1, 497]]
points4 = [[0,0], [-2,0], [4,0], [1,1], [3,3], [-2,2], [5,2]]
print("nlogn", closestPair(points4))