# coding=utf-8
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) < 1:
            self.min_stack.append(x)
            return x
        self.min_stack.append(min(self.min_stack[-1], x))
        return x

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        return None

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min_stack[-1]

a = MinStack()
a.push(-2)
print a.top
print a.getMin()