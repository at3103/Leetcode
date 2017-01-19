class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        strt = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                cnt = i - strt 
                strt = i + 1
                if cnt > max:
                    max = cnt
                if max > (l-i + 1):
                    break
            elif i == l-1:
                cnt = i - strt + 1
                if cnt > max:
                    max = cnt

        return max