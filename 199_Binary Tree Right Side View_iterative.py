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

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, node):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not node:
            return []

        right_view = list([node.val])

        lvl = deque()
        lvl.append(node)

        while lvl:
            lvl1 = deque()
            while lvl:
                cur = lvl.popleft()
                if cur.left:
                    lvl1.append(cur.left)
                if cur.right:
                    lvl1.append(cur.right)
            if lvl1:
                right_view.append(lvl1[-1].val)

            lvl = lvl1
        return right_view