def isMonotonic(array):
    # Write your code here.
    if len(array)==0 or len(array)==1:
        return True

    isReversed = True if array[0]>array[-1] else False

    for index in range(1, len(array)):
        if not isReversed:
            if array[index]<array[index-1]:
                return False
        else:
            if array[index]>array[index-1]:
                return False
    
    return True