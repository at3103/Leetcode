"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.

"""

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def level_order(node, lvl_dict, lvl):
    
    if not node:
        return lvl_dict
    
    lvl_dict[lvl] = node.val
    
    lvl_dict = level_order(node.left, lvl_dict, lvl+1)
    lvl_dict = level_order(node.right, lvl_dict, lvl+1)
    
    return lvl_dict
    

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lvl_dict = defaultdict(list)
        
        return level_order(root, lvl_dict,0).values()