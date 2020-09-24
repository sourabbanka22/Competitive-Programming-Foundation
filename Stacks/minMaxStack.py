# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = [{"min": float("inf"), "max": float("-inf")}]

    def peek(self):
        # Write your code here.
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
        self.stack.append(number)
        minimum = min(number, self.minMaxStack[-1]["min"])
        maximum = max(number, self.minMaxStack[-1]["max"])
        self.minMaxStack.append({"min": minimum, "max": maximum})

    def getMin(self):
        # Write your code here.
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        # Write your code here.
        return self.minMaxStack[-1]["max"]

minMaxStack = MinMaxStack()
minMaxStack.push(1)