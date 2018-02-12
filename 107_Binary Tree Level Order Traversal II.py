"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
def lvl_order_helper(node, lvl_dict, lvl):
    
    if not node:
        return lvl_dict
    lvl_dict[lvl].append(node.val)
    lvl_dict = lvl_order_helper(node.left, lvl_dict, lvl+1)
    lvl_dict = lvl_order_helper(node.right, lvl_dict, lvl+1)
    return lvl_dict

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lvl_dict = defaultdict(list)
        lvl = 0
        lvl_dict = lvl_order_helper(root, lvl_dict, lvl)
        return lvl_dict.values()[::-1]