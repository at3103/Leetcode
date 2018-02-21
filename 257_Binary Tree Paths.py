"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def binTreePathHelper(node):
    
    if not node:
        return []
     
    ret_paths = ["{}->{}".format(node.val, x) for x in binTreePathHelper(node.left)]
    
    ret_paths.extend(["{}->{}".format(node.val, x) for x in binTreePathHelper(node.right)])
    
    return ret_paths if ret_paths else [str(node.val)]

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        return binTreePathHelper(root)
        