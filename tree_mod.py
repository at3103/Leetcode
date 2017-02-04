# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter,deque,defaultdict
class Solution(object):
	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		tree =defaultdict()
		temp = root
		mod = -1
		mod_list =[]
		to_traverse = deque()

		while temp:
			val = temp.val
			if not tree.get(val):
				tree[val]=1
			else:
				tree[val]+=1
			if tree[val] > mod:
				mod = tree[val]
				mod_list =[val]
			elif tree[val] == mod:
				mod_list.append(val)
			if temp.left:
			    to_traverse.append(temp.left)
			if temp.right:
			to_traverse.append(temp.right)
			temp = to_traverse.pop()

		return mod_list
				
				
				
		#count_dict = Counter(