"""
This is from leetcode competition
"""
from collections import deque

class Solution(object):
    """
    This class is for solution
    """
    @classmethod
    def __init__(cls):
        """
        Constructor
        """
        self.tree_traversal = deque()

    @classmethod
    def find_left_most_node(cls, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        levels = []
        self.tree_traversal.append([root, 1])
        current_level = 0
        level = 0
        left_most_value = root.val

        while self.tree_traversal:
            current, current_level = self.tree_traversal.pop()
            current_level += 1
            if current.right:
                self.tree_traversal.append([current.right, current_level])
                if level < current_level and not current.left:
                    level = current_level
                    left_most_value = current.right.val
            if current.left:
                self.tree_traversal.append([current.left, current_level])
                if level < current_level:
                    level = current_level
                    left_most_value = current.left.val
        return left_most_value
            