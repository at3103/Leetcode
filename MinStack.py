from collections import deque
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = -1
        self.min_list = deque()
        self.stack=list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.stack) == 1:
            self.min = x
        elif x <= self.min:
            self.min_list.append(self.min)
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.min == self.stack[-1]:
            if len(self.min_list):
                self.min = self.min_list.pop()
            else:
                self.min = self.stack[0]
        if len(self.stack):   
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()