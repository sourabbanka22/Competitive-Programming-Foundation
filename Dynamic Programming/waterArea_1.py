def waterArea(heights):
    # Write your code here.
    left = [0 for _ in heights]
    right = [0 for _ in heights]

    for index in range(1, len(heights)):
        if heights[index]<heights[index-1] and left[index-1]<heights[index-1]:
            left[index] = heights[index-1]
        else:
            left[index] = left[index-1]
    for index in reversed(range(len(heights)-1)):
        if heights[index]<heights[index+1] and right[index+1]<heights[index+1]:
            right[index] = heights[index+1]
        else:
            right[index] = right[index+1]
    
    result = 0
    for index in range(len(heights)):
        possibleSurfaceArea = min(left[index], right[index])-heights[index]
        if possibleSurfaceArea>=0:
            result += possibleSurfaceArea
    
    return result

print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))