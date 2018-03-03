"""

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        

        res = list()
        cur = root
        
        while cur:
            
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                # Now cur has a left node/left subtree
                pre = cur.left
                
                # Find the right most node of the left subtree
                while pre.right:
                    pre = pre.right
                
                # Shift the current node to the right of the the rightmost node
                pre.right = cur
                
                # Save the current node
                temp = cur
                cur = cur.left
                temp.left = None
        return res
        