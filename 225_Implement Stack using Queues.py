from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.t = -1

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        self.t = x
        
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            self.stack = deque(reversed(self.stack))
            self.stack.popleft()
            self.stack=deque(reversed(self.stack))
        if not self.empty():
            self.t = self.stack[-1]
        else:
            self.t=-1

    def top(self):
        """
        :rtype: int
        """
        return self.t
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
        