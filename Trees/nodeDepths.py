def nodeDepths(root):
    # Write your code here.
    
    return nodeDepthsUtil(root, depth=0)

def nodeDepthsUtil(node, depth):
    if node.left is None and node.right is None:
        return depth
    elif node.left is not None and node.right is not None:
        return depth + nodeDepthsUtil(node.left, depth + 1) + nodeDepthsUtil(node.right, depth + 1)
    elif node.left is not None:
        return depth + nodeDepthsUtil(node.left, depth + 1)
    elif node.right is not None:
        return depth + nodeDepthsUtil(node.right, depth + 1)
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

