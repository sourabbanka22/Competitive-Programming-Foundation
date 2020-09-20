def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    result = [0, 0]
    arrayOne.sort()
    arrayTwo.sort()
    left, right = 0, 0
    diff = float("inf")

    while left < len(arrayOne) and right < len(arrayTwo):
        if abs(arrayOne[left]-arrayTwo[right])<diff:
            result[0], result[1] = arrayOne[left], arrayTwo[right]
            diff = abs(arrayOne[left]-arrayTwo[right])
        if arrayOne[left]>arrayTwo[right]:
            right += 1
        else:
            left += 1

    return result

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))