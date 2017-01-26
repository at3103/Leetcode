class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		#Initialize prev,maximum sum (max_s) and compute length of nums
		l = len(nums)
		prev = nums[0]
		max_s = prev

		for i in range(1,l):
		    prev = (prev > 0) * prev + nums[i]
		#Check if the newly computed prev is greater than old max_s and modify max_s accordingly
		    if prev > max_s:
		        max_s = prev
		return max_s

S = Solution()
print S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

'''
[-2,1,-3,4,-1,2,1,-5,4]
[1]
[0]
[-1]
[8,-19,5,-4,20]
'''