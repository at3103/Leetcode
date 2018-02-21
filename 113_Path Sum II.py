"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        stack = deque()
        
        ret_paths = list()
        
        if not root:
            return ret_paths
        
        stack.append((root, sum, []))
        
        while stack:
            
            cur, tgt, path = stack.pop()
            
            path.append(cur.val)
            tgt -= cur.val
            
            # Leaf node conditions and if it's val equlas target, then this path is a desired path.
            if not cur.left and not cur.right and tgt == 0:
                ret_paths.append(path)
            else:
                # If valid cur.left, add cur.left, new target and a copy of the path
                if cur.left:
                    stack.append((cur.left, tgt, list(path)))
                
                # If valid cur.right, add cur.right, new target and a copy of the path
                if cur.right:
                    stack.append((cur.right, tgt, list(path)))
        
        return ret_paths
        