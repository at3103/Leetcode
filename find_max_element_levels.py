"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
from collections import deque,defaultdict

class Solution(object):
    def find_value_most_element(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        TreeTraversal = deque()
        TreeTraversal.append([root,0])
        retlist = list()
        size = 0
        current_level = 0
        retlist.append(root.val)
        while TreeTraversal:
            current,current_level = TreeTraversal.pop()
            if size < current_level + 1:
                retlist.append(-2147483648)
                size += 1
            current_level += 1
            if current.right:
                TreeTraversal.append([current.right,current_level])
                if current.right.val > retlist[current_level]:
                    retlist[current_level] = current.right.val
            if current.left:
                TreeTraversal.append([current.left,current_level])
                if current.left.val > retlist[current_level]:
                    retlist[current_level] = current.left.val
        retlist.pop()
        return retlist
            
        