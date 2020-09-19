def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    if n==0:
        return 1
    numOfTrees = 0
    for left in range(n):
        right = n-1-left
        numOfLeftTrees = numberOfBinaryTreeTopologies(left)
        numOfRightTrees = numberOfBinaryTreeTopologies(right)
        #print("Tree Size: " + str(n) + " Left: " + str(numOfLeftTrees) + " Right: " + str(numOfRightTrees))
        numOfTrees += numOfLeftTrees*numOfRightTrees
    return numOfTrees

print(numberOfBinaryTreeTopologies(3))