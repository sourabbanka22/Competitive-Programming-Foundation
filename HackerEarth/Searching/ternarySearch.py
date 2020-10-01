
def ternarySearch(left, right, key, array):
    
    while right>=left:
        oneThird = left + (right-left)//3
        twoThird = right - (right-left)//3
        if array[oneThird] == key:
            return oneThird
        elif array[twoThird] == key:
            return twoThird
        elif key<array[oneThird]:
            right = oneThird-1
        elif key>array[twoThird]:
            left = twoThird+1
        else:
            left = oneThird+1
            right = twoThird-1

    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 24, 45, 65, 100]
print(ternarySearch(0, len(array)-1, 65, array))

