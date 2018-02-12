"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(node):
    
    if not node:
        return 0
    dist_left = float('inf')
    dist_right = float('inf')
    
    if node.left:
        dist_left = dfs(node.left)
    if node.right:
        dist_right = dfs(node.right)

    min_depth = 1 + (0 if (dist_left == float('inf') and dist_right == float('inf')) else min(dist_left, dist_right))
    return min_depth

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root)