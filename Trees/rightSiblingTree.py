# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def rightSiblingTree(root):
    # Write your code here.
    rightSiblingTreeUtil(root, None)
    return root

def rightSiblingTreeUtil(node, parent):
    left = node.left
    right = node.right
    
    if left is not None:
        rightSiblingTreeUtil(left, node)

    if parent is None:
        node.right = None
    elif parent.left == node:
        node.right = parent.right
    elif parent.right is None:
        node.right = None
    else:
        node.right = parent.right.left
    
    if right is not None:
        rightSiblingTreeUtil(right, node)