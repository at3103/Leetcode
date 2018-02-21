"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        stack = deque()
        visited = set()
        
        if not root:
            return False
        
        stack.append((root, sum))
        
        
        while stack:# or cur:
            
            cur, tgt = stack.pop()
                
            if not cur.left and not cur.right and tgt == cur.val:
                return True
            
            if cur.left:
                stack.append((cur.left, tgt - cur.val))
            if cur.right:            
                stack.append((cur.right, tgt - cur.val))
            
        
        return False