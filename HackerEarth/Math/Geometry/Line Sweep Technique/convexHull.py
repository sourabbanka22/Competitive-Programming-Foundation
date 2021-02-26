import math

def slopeOfLine(A, B):
    numerator = B[1]-A[1]
    denominator = B[0]-A[0]
    print([A, B], numerator/denominator)
    return numerator/denominator

def angleBetweenLines(slope1, slope2):
    numerator = slope2-slope1
    denominator = 1 + slope1*slope2
    return math.degrees(math.atan(abs(numerator/denominator)))

def sortFunction(minYPoint, x):
    slope1 = slopeOfLine(minYPoint, [minYPoint[0]+1, minYPoint[1]])
    slope2 = slopeOfLine(minYPoint, x)
    return angleBetweenLines(slope1, slope2)

def sortByAngle(points, minYPoint):
	points.sort(key=lambda x: sortFunction(minYPoint, x))
	return points

def getDirection(A, B, C, D):
    
    x1 = B[0]-A[0]
    y1 = B[1]-A[1]
    x2 = D[0]-C[0]
    y2 = D[1]-C[1]

    if x1*y2 > y1*x2:
        return "Counter-ClockWise"
    elif x1*y2 < y1*x2:
        return "ClockWise"
    else:
        return "Collinear"

def convexHull(points):

    minYPoint = min(points, key = lambda x: x[1])
    points.remove(minYPoint)
    points = [minYPoint] + sortByAngle(points, minYPoint)
    return points

points = [[2, 2], [-2, 3], [1, 1], [3, 3]]
print(convexHull(points))

