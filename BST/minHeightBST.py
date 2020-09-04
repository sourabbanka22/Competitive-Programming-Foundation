def minHeightBst(array):
    root = None
    return minHeightBstUtil(array, root, 0, len(array)-1)

def minHeightBstUtil(array, root, left, right):

    if left > right:
        return
    mid = (left + right)//2
    if root == None:
        root = BST(array[mid])
    else:
        root.insert(array[mid])

    minHeightBstUtil(array, root, left, mid-1)
    minHeightBstUtil(array, root, mid+1, right)

    return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
