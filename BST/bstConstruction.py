class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		currentNode = self
		while True:
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self

	def contains(self, value):
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else:
				return True
		return False

	def remove(self, value, parentNode=None):
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				paretNode = currentNode
				currentNode = currentNode.right
			else:
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value = currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value, currentNode)
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						currentNode.value = None
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
		return self

	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value
	
	def inOrder(self):
		array = []
		return self.inOrderUtil(array)

	def inOrderUtil(self, array):
		if self == None:
			return
		if self.left != None:
			self.left.inOrderUtil(array)
		array.append(self.value)
		if self.right != None:
			self.right.inOrderUtil(array)

		return array

root = BST(50)
root.insert(30) 
root.insert(20) 
root.insert(40) 
root.insert(70) 
root.insert(60) 
root.insert(80)

print(root.inOrder())

print ("Delete 20")
root.remove(20)
print("inOrder traversal of the modified tree")
print(root.inOrder())
  
print("Delete 30")
root.remove(30) 
print("inOrder traversal of the modified tree")
print(root.inOrder())
  
print("Delete 50")
root.remove(50)
print("inOrder traversal of the modified tree")
print(root.inOrder())


root = BST(1)
root.insert(3) 
root.insert(4) 
print("Initial", root.inOrder())
root.remove(4)
print("inOrder traversal of the modified tree after removing 4")
print(root.inOrder())

root.remove(1)
print("inOrder traversal of the modified tree after removing 1")
print(root.inOrder())

root.remove(3)
print("inOrder traversal of the modified tree after removing 3")
print(root.inOrder())