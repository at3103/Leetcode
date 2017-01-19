class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fset = set(range(1,len(nums)+1))
        return list(fset - set(nums))
        