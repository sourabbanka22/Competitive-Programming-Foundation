# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		# Write your code here.
		# Do not edit the return statement of this method.
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

	def contains(self, value):
		# Write your code here.
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else:
				return True
		return False

	def remove(self, value):
		current = self
		if current == None:
			return current
		
		if value < current.value:
			current.left = current.left.remove(value)
		elif value > current.value:
			current.right = current.right.remove(value)
		else:
			if current.left == None:
				return current.right
			elif current.right == None:
				return current.left
			
			minValue = current.right.getMinValue()
			current.value = minValue

			current.right = current.right.remove(minValue)

		return current
	
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

	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		
		return currentNode.value

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