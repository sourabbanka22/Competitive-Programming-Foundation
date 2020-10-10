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

print(getDirection([1, 1], [5, 4], [4, 1], [8, 4]))