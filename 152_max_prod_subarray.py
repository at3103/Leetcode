class Solution(object):
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		#Initialize prev,maximum sum (max_s) and compute length of nums
		l = len(nums)
		prev = 1
		max_s = nums[0]
		i=0

		while i <l:
			t = nums[i+1] if (i < l-1) else 1
			if (prev * nums[i]*t) > 0 and i < l-1:
				prev*=nums[i]*t
				i+=2
			elif (prev * nums[i] * t) > 0:
				prev*=nums[i]
				i+=1
			elif nums[i]*nums[i-1] > 0 :
				prev = nums[i]*nums[i-1]
				i+=1
			else:
				prev = nums[i]
				i+=1
		#Check if the newly computed prev is greater than old max_s and modify max_s accordingly
			if prev > max_s:
				max_s = prev
		return max_s

S = Solution()
print S.maxProduct([-2,1,-3,4,-1,2,1,-5,4])

'''
[-2,1,-3,4,-1,2,1,-5,4]
[1]
[0]
[-1]
[8,-19,5,-4,20]
'''