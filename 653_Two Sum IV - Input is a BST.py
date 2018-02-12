"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def searchBST(node, first, num):
    if not node:
        return False
    if node.val == num and node != first:
        return True
    elif node.val > num:
        return searchBST(node.left, first, num)
    else:
        return searchBST(node.right, first, num)

def traverseBST(root,node, target):
    if not node:
        return False
    if searchBST(root, node, target-node.val) or searchBST(root, node, target-node.val):
        return True
    elif traverseBST(root, node.left, target):
        return True
    else:
        return traverseBST(root, node.right, target)
    
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return traverseBST(root, root, k)
        