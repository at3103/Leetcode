"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        lvl = deque()
        if root.left:
            lvl.append(root.left)
        if root.right:
            lvl.append(root.right)
        
        while True:
            prev = None
            lvl1 = deque()
            while lvl:
                cur = lvl.popleft()
                if prev:
                    prev.next = cur
                if cur.left:
                    lvl1.append(cur.left)
                if cur.right:
                    lvl1.append(cur.right)

                prev = cur
            if not lvl1:
                break
            lvl = lvl1                
