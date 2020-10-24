import math

def findDistance(point1, point2):
    yDist = (point2[1]-point1[1])*(point2[1]-point1[1])
    xDist = (point2[0]-point1[0])*(point2[0]-point1[0])
    return math.sqrt(xDist+yDist)

def naiveClosestPair(points):

    best = float("inf")
    for idx1 in range(len(points)):
        for idx2 in range(idx1+1, len(points)):
            distance = findDistance(points[idx1], points[idx2])
            if best > distance:
                best = distance
                pair = [points[idx1], points[idx2]]
    return (best, pair)


points = [[0, 5], [5, 1], [2, 3], [4, 2]]
print("n^2", naiveClosestPair(points))
print("")
print(closestPair(points))