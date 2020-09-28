def maxPathSum(tree):
	maxSum = findMaxSum(tree)
    return maxSum[1]

def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBrach = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNoode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBrach)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNoode)

    return (maxSumAsBrach, maxPathSum)