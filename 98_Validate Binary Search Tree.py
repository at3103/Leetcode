"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(node, min_val, max_val):
            
            if not node:
                return True
            
            if node.val <= min_val or node.val >= max_val:
                return False
            
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
        
        return helper(root, float("-inf"), float("inf"))

