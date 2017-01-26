from collections import deque
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        opt=[0]*l
        opt[0] = nums[0]
        max_s = 0
        for i in range(1,l):
            temp = 0 if 0 > opt[i-1] else opt[i-1]
            opt[i] = temp + nums[i]
            if opt[i] > opt[max_s]:
                max_s = i
        
        retlist = deque()
        temp = opt[max_s]
        i = max_s

        while temp > 0 and i >= 0:
            retlist.appendleft(nums[i])
            temp-=nums[i]
            i-=1
        return list(retlist)
        

S = Solution()
print S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])