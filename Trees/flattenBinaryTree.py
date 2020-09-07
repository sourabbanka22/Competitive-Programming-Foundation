# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
    leftMost, _ = flattenBinaryTreeUtil(root)
    return leftMost

def flattenBinaryTreeUtil(node):

    if node.left == None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenBinaryTreeUtil(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost
    
    if node.right == None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenBinaryTreeUtil(node.right)
        connectNodes(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRightMost
    
    return [leftMost, rightMost]

def connectNodes(left, right):
    left.right = right
    right.left = left