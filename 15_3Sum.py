"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums_old):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums_old)
        
        res = list()
        
        if n < 3:
            return res
    
        nums = sorted(nums_old)
        prev_num = float("-inf")
        for a, num1 in enumerate(nums[:-2]):
            
            # First number is too small or same as prev number.
            if num1 == prev_num or num1 + sum(nums[-2:]) < 0:
                continue
            
            # First number is too large.
            if num1 + sum(nums[a+1:a+3]) > 0:
                break
            
            l = a+1
            r = n-1
            
            while l<r:
                s = nums[l] + nums[r]
                if s + num1 < 0:
                    l += 1
                elif s + num1 > 0:
                    r -= 1
                else:
                    res.append([num1, nums[l], nums[r]])
                    
                    while l<n-1 and nums[l+1] == nums[l]:
                        l += 1
                    while r>0 and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
            prev_num = num1
        return res