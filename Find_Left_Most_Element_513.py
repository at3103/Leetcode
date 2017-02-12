from collections import deque

class Solution(object):
    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        TreeTraversal = deque()
        levels = []
        TreeTraversal.append(root)
        levels.append(root.val)
        current_level = 0
        level = 0
        left_most_value = root.val

        while TreeTraversal:
            current = TreeTraversal.pop()
            current_level += 1
            if not current.left and not current.right:
                current_level = 1
                continue
            if current.right:
                TreeTraversal.append(current.right)
                if level < current_level and not current.left:
                    level = current_level
                    left_most_value = current.left.val
            if current.left:
                TreeTraversal.append(current.left)
                if level < current_level:
                    level = current_level
                    left_most_value = current.left.val
        return left_most_value
            