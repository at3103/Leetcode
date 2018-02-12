"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        f = -1
        res = list()
        lvl = deque()
        lvl.append(root)
        res.append([root.val])
        
        while lvl:
            lvl1 = list()
            while lvl:
                cur = lvl.popleft()
                if cur.left:
                    lvl1.append(cur.left)
                if cur.right:
                    lvl1.append(cur.right)
            lvl = deque(lvl1)
            lvl1 = lvl1[::f]
            if lvl1:
                res.append([cur.val for cur in lvl1])
            
            f *= -1
        
        return res
                                        