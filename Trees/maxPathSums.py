class MaxSum:
	def __init__(self, maxSumAsBranch, maxSum):
		self.maxSumAsBranch = maxSumAsBranch
		self.maxSum = maxSum

def maxPathSum(tree):
    # Write your code here.
    maxSumClass = MaxSum(float("-inf"), float("-inf"))
    maxSumClass = maxPathSumUtil(tree, maxSumClass)
    return maxSumClass.maxSum

def maxPathSumUtil(tree, maxSumClass):
	if tree.left is None and tree.right is None:
		maxSumClass.maxSumAsBranch = tree.value
		maxSumClass.maxSum = tree.value
		return maxSumClass
	
	if tree.right:
		rightSubTreeClass = maxPathSumUtil(tree.right, maxSumClass)
		rightSubTreeMax = rightSubTreeClass.maxSumAsBranch
	else:
		rightSubTreeMax = float("-inf")
	if tree.left:
		leftSubTreeClass = maxPathSumUtil(tree.left, maxSumClass)
		leftSubTreeMax = leftSubTreeClass.maxSumAsBranch
	else:
		leftSubTreeMax = float("-inf")
	
	currentNode = tree.value
	combined = leftSubTreeMax + currentNode + rightSubTreeMax
	leftWithRoot = currentNode + leftSubTreeMax
	rightWithRoot = currentNode + rightSubTreeMax
	maxSumClass.maxSumAsBranch = max(currentNode, leftWithRoot, rightWithRoot)
	maxSumClass.maxSum = max(currentNode, leftWithRoot, rightWithRoot, combined)
	return maxSumClass