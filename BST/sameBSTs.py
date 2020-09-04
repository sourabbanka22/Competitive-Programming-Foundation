class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		currentNode = self
		while True:
			if value < currentNode.value:
				if currentNode.left == None:
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:
				if currentNode.right == None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self

	def preOrder(self):
		array = []
		return self.preOrderUtil(array)
	
	def preOrderUtil(self, array):
		if self == None:
			return
		array.append(self.value)
		if self.left != None:
			self.left.preOrderUtil(array)
		if self.right != None:
			self.right.preOrderUtil(array)

		return array

def sameBsts(arrayOne, arrayTwo):
	# Write your code here.
	treeOne = BST(arrayOne[0])
	for node in arrayOne:
		treeOne.insert(node)

	treeTwo = BST(arrayTwo[0])
	for node in arrayTwo:
		treeTwo.insert(node)

	return treeOne.preOrder() == treeTwo.preOrder()

print(sameBsts([5, 2, -1, 100, 45, 12, 8, -1, 8, 10, 15, 8, 12, 94, 81, 2, -34], [5, 8, 10, 15, 2, 8, 12, 45, 100, 2, 12, 94, 81, -1, -1, -34, 8]))

print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 10], [10, 8, 5, 15, 2, 10, 12, 94, 81]))