class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.leftSubtreeSize = 0

	def insert(self, value, result, index):
		currentNode = self
		rightSmallerThan = 0
		while True:
			if value < currentNode.value:
				currentNode.leftSubtreeSize += 1
				if currentNode.left == None:
					currentNode.left = BST(value)
					result[index] = rightSmallerThan
					break
				else:
					currentNode = currentNode.left
			else:
				rightSmallerThan += currentNode.leftSubtreeSize
				if value > currentNode.value:
					rightSmallerThan += 1
				if currentNode.right == None:
					currentNode.right = BST(value)
					result[index] = rightSmallerThan
					break
				else:
					currentNode = currentNode.right
		return self


def rightSmallerThan(array):
	# Write your code here.
	result = array[:]
	if len(array) != 0:
		result[-1] = 0
		tree = BST(array[-1])
	for index in reversed(range(len(array)-1)):
		tree.insert(array[index], result, index)

	return result

print(rightSmallerThan([8, 5, 11, -1, 3, 4, 2]))
# result [5, 4, 4, 0, 1, 1, 0]