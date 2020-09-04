def findClosestValueInBst(tree, target):
    # Write your code here.
    current = tree
    diff = float("inf")
    closestValue = None
    while current != None:
        if abs(target - current.value) < diff:
            diff = abs(target - current.value)
            closestValue = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        elif target == current.value:
            return target
        
    return closestValue


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
