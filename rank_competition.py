from collections import defaultdict

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        retlist = []
        Medals = {0:"Gold Medal", 1:"Silver Medal",2: "Bronze Medal"}
        
        positions = defaultdict()
        n = len(nums)
        for i in range(n):
            positions[nums[i]] = i
            
        sort_scores = sorted(nums,reverse = True)
        
        for i in range(n):
            retlist.append(Medals.get(i,str(i+1)))
            
        return retlist
                
        