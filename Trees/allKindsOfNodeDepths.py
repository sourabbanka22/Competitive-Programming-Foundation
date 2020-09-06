def allKindsOfNodeDepths(root):
    # Write your code here.
    result = 0
    stack = []
    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        elif len(stack) != 0:
            top = stack.pop()
            result += getDepth(top, depth=0)
            root = top.right
        else:
            break
    
    return result

def getDepth(node, depth):
    if node.left == None and node.right == None:
        return depth
	elif node.left != None and node.right != None:
        return depth + getDepth(node.left, depth+1) + getDepth(node.right, depth+1)
    elif node.left is not None:
        return depth + getDepth(node.left, depth+1)
    elif node.right is not None:
        return depth + getDepth(node.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
