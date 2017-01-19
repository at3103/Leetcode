class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #retlist=list()
        blist = [0]*len(nums)
        for i in nums:
            blist[i-1] += 1
        
        nums = blist
        blist=list()
        for i in range(len(nums)):
            if nums[i] == 2:
                blist.append(i+1)
        return blist