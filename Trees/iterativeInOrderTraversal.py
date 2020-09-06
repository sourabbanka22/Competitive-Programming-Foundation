def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    stack = []
    while True:
        if tree is not None:
            stack.append(tree)
            tree = tree.left
        elif len(stack) != 0:
            top = stack.pop()
            callback(top)
            tree = top.right
        else:
            break
