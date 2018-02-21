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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def hasPathSumHelper(node, tgt):
    """
    :type node: TreeNode
    :type tgt: int
    :rtype: bool
    """    
    if not node:
        return False
    
    if not node.left and not node.right:
        return tgt == node.val
    
    tgt -= node.val
    
    return hasPathSumHelper(node.left, tgt) or hasPathSumHelper(node.right, tgt)
    

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return hasPathSumHelper(root, sum)