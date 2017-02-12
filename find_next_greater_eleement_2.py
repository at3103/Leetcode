class Solution(object):
	def __init__(self):
		self.retlist = []
		self.max_ele = 0
		self.n =0
		self.to_add = 0

	def nextGreaterElements(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums:
			return self.retlist
		self.max_ele = max(nums)
		self.n = len(nums)
		for temp_indx in range(self.n):
			i = nums[temp_indx]
			if i == self.max_ele:
				self.retlist.append(-1)
				continue
			self.to_add = self.max_ele + 1
			for j in nums[temp_indx+1 :]:
				if j > i:
					self.to_add = j
					break
			if self.to_add == self.max_ele + 1:
				for j in nums[: temp_indx]:
					if j > i:
						self.to_add = j
						break
			self.retlist.append(self.to_add)
			
		return self.retlist

S = Solution()

print S.nextGreaterElements([1,2,1])