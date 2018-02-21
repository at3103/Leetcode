"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = deque()
        path_sums = 0
        stack.append((root,str(root.val)))
        
        while stack:
            cur, num = stack.pop()
            
            if not cur.left and not cur.right:
                path_sums += int(num)
            if cur.left:
                stack.append((cur.left, num+str(cur.left.val)))
            if cur.right:
                stack.append((cur.right, num+str(cur.right.val)))

        return path_sums