# Write your code here
def getHexSum(value):
    mapper = {
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15
    }
    valList = list(hex(value).lstrip("0x"))
    summation = 0
    for val in valList:
        if val in mapper:
            summation += mapper[val]
        else:
            summation += int(val)
    return summation

def getGCD(a, b):
    while b:
        a, b= b, a%b
    return a

def isTrue(X):
    fX = getHexSum(X)
    return getGCD(X, fX)>1

cases = int(input())
for case in range(cases):
    left, right = map(int, input().split())
    count = 0
    for index in range(left, right+1):
        if isTrue(index):
            count += 1
    print(count)