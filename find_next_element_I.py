class Solution(object):
	def nextGreaterElement(self, findNums, nums):
		"""
		:type findNums: List[int]
		:type nums: List[int]
		:rtype: List[int]
		"""
		retlist = []
		for i in findNums:
			temp_indx = nums.index(i)
			to_add = -1
			for j in nums[temp_indx+1 :]:
				if j > i:
					to_add = j
					break
			retlist.append(to_add)
			
		return retlist