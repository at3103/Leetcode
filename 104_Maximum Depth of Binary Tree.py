"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(node):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    if not node:
        return 0
    
    dist_right = float('-inf')
    dist_left = float('-inf')
    
    if node.left:
        dist_left = dfs(node.left)
    if node.right:
        dist_right = dfs(node.right)        
    
    return 1 + (0 if (dist_left == float('-inf') and dist_right == float('-inf')) else max (dist_left,dist_right))

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return dfs(root)
        