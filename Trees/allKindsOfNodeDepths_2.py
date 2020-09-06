def allKindsOfNodeDepths(root):
    # Write your code here.
    calculateChildrens(root)
    calculateDepths(root)
    printInorder(root)
    result = getAllKindsOfNodeDepths(root)
    return result

def getAllKindsOfNodeDepths(node):
    if node.left == None and node.right == None:
        return node.depth
    elif node.left != None and node.right != None:
        return node.depth + getAllKindsOfNodeDepths(node.left) + getAllKindsOfNodeDepths(node.right)
    elif node.left is not None:
        return node.depth + getAllKindsOfNodeDepths(node.left)
    elif node.right is not None:
        return node.depth + getAllKindsOfNodeDepths(node.right)

def calculateChildrens(root):
    if root.left == None and root.right == None:
        root.children = 1
    elif root.left != None and root.right != None:
        root.children = 1 + calculateChildrens(root.left) + calculateChildrens(root.right)
    elif root.left is not None:
        root.children = 1 + calculateChildrens(root.left)
    elif root.right is not None:
        root.children = 1 + calculateChildrens(root.right)
    return root.children

def calculateDepths(root):
    if root.left == None and root.right == None:
        root.depth = 0
        return
    elif root.left != None and root.right != None:
        calculateDepths(root.left)
        calculateDepths(root.right)
        root.depth = root.left.children + root.left.depth + root.right.children + root.right.depth
    elif root.left is not None:
        calculateDepths(root.left)
        root.depth = root.left.children + root.left.depth
    elif root.right is not None:
        calculateDepths(root.right)
        root.depth = root.right.children + root.right.depth

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.children = 0
        self.depth = 0
        self.left = None
        self.right = None

def printInorder(node):
    if node is not None:
        printInorder(node.left)
        print("Children: " + str(node.children) + " Depth: " + str(node.depth))
        printInorder(node.right)


node = BinaryTree(3)
node.left = BinaryTree(4)
node.right = BinaryTree(5)
node.left.left = BinaryTree(6)
node.left.right = BinaryTree(7)
node.right.left = BinaryTree(8)
node.right.right = BinaryTree(9)

print("Result: "+str(allKindsOfNodeDepths(node)))