"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def level_order_helper(node, lvl_dict, lvl):
    
    if not node:
        return lvl_dict
    
    lvl_dict[lvl].append(node.val)
    
    lvl_dict = level_order_helper(node.left, lvl_dict, lvl+1)
    lvl_dict = level_order_helper(node.right, lvl_dict, lvl+1)
    
    return lvl_dict
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        lvl = 0
        lvl_dict = defaultdict(list)
        
        lvl_dict = level_order_helper(root, lvl_dict, lvl)
        return list(lvl_dict.values())