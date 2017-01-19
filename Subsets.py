from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retlist = [[]]
        
        for k in range(1,len(nums)+1):
            retlist.extend(list(combinations(nums,k)))
            
        return retlist