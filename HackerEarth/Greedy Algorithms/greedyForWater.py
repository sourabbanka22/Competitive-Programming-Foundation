cases = int(input())
for case in range(cases):
    noOfBottles, capacity = map(int, input().split())
    bottles = list(map(int, input().split()))
    bottles.sort()
    currentBottles = 0
    currentFilled = 0
    for bottleIdx in range(noOfBottles):
        if currentFilled+bottles[bottleIdx]<=capacity:
            currentFilled += bottles[bottleIdx]
            currentBottles += 1
        else:
            break
    print(currentBottles)