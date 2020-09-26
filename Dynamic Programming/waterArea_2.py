def waterArea(heights):
    # Write your code here.
    if len(heights)==0:
        return 0
    leftIdx = 0
    rightIdx = len(heights)-1
    leftMaxHeight = heights[leftIdx]
    rightMaxHeight = heights[rightIdx]
    surfaceArea = 0

    while leftIdx<rightIdx:
        if heights[leftIdx]<heights[rightIdx]:
            leftIdx += 1
            leftMaxHeight = max(leftMaxHeight, heights[leftIdx])
            surfaceArea += leftMaxHeight-heights[leftIdx]
        else:
            rightIdx-=1
            rightMaxHeight = max(rightMaxHeight, heights[rightIdx])
            surfaceArea += rightMaxHeight-heights[rightIdx]
    
    return surfaceArea

print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))