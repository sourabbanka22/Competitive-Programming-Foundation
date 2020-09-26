def minNumberOfJumps(array):
    # Write your code here.
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for index in range(1, len(array)-1):
        maxReach = max(maxReach, index+array[index])
        steps -= 1
        if steps==0:
            jumps += 1
            steps = maxReach-index
    
    return jumps+1

print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))