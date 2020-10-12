import math

def getCoefficients(P, Q):
    a = Q[1]-P[1]
    b = P[0]-Q[0]
    c = -(a*P[0]+b*P[1])
        
    return (a, b, c)

def findDistance(X, coefficients):
    numerator = abs(coefficients[0]*X[0] + coefficients[1]*X[1] + coefficients[2])
    denominator = math.sqrt(coefficients[0]*coefficients[0] + coefficients[1]*coefficients[1])

    return numerator/denominator

P = [3, 2]
Q = [2, 6]
coefficients = getCoefficients(P, Q)
X = [-1, 3]
print(findDistance(X, coefficients))