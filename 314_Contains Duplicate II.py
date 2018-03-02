"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""

from collections import defaultdict
from functools import reduce

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        nums_index_dict = reduce(lambda acc, x: acc[x[1]].append(x[0]) or acc, enumerate(nums),defaultdict(list))

        for num, val in nums_index_dict.items():
            
            if len(val) <=1:
                continue
            
            for i in range(1,len(val)):
                if val[i] - val[i-1] <= k:
                    return True
        return False
            