from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        C = Counter(nums)
        
        for k in C.keys():
            if C[k] > (len(nums)/2):
                return k
        