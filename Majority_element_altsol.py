from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)/2
        for i in set(nums):
            if nums.count(i) > l:
                return i

        