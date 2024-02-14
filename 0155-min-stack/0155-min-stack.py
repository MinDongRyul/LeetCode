class MinStack(object):

    def __init__(self):
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.min_stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()