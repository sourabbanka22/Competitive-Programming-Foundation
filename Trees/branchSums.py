# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    return branchSumsUtil(root, 0, [])

def branchSumsUtil(root, current, array):
    if root == None:
        return

    if root.left == None and root.right == None:
        array.append(current + root.value)
        return array

    branchSumsUtil(root.left, current + root.value, array)
    branchSumsUtil(root.right, current + root.value, array)

    return array
