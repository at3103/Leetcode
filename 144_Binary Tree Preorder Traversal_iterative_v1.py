"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

"""
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        stack = deque()
        res = list()
        visited = set()
        
        stack.append(root)
        
        while stack:
            cur = stack.pop()
            
            if cur in visited:
                res.append(cur.val)
                continue
                
            visited.add(cur)
            
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            stack.append(cur)
        
        return res
        