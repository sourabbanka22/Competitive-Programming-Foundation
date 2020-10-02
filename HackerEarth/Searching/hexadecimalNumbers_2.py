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

memo = [0]*100001
for index in range(1, 100001):
    fX = getHexSum(index)
    if getGCD(index, fX)>1:
        memo[index] = 1

for index in range(1, 100001):
    memo[index] += memo[index-1]

cases = int(input())
for case in range(cases):
    left, right = map(int, input().split())
    count = memo[right]-memo[left-1]
    print(count)