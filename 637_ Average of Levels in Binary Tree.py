"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

"""

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lvl_order_traversal(node, lvl_dict, lvl):
    
    if not node:
        return lvl_dict
    
    lvl_dict[lvl].append(node.val)
    
    lvl_dict = lvl_order_traversal(node.left, lvl_dict, lvl+1)
    lvl_dict = lvl_order_traversal(node.right, lvl_dict, lvl+1)
    return lvl_dict

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        lvl = 0
        lvl_dict = defaultdict(list)
        
        lvl_dict = lvl_order_traversal(root, lvl_dict, lvl)
        return [sum(lvl)/len(lvl) for lvl in lvl_dict.values()]