from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        smax=list()
        if len(nums) == 0 or k ==0:
            return smax
        temp =deque(nums[:k])
        tmax = max(temp)
        smax.append(tmax)
        for i in range(k,len(nums)):
            temp.append(nums[i])
            if tmax < nums[i]:
                temp.clear()
                temp = deque([nums[i]])
                tmax=nums[i]
            elif temp.popleft() == tmax:
                tmax = max(temp)
            smax.append(tmax)
        return smax
        