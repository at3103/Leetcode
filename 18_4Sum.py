"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums_old, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums_old)
        
        if n < 4:
            return []
        
        res = list()
        
        nums= sorted(nums_old)

        prev_a = float("-inf")
        for a in range(n-3):
            if nums[a] == prev_a:
                continue
            # a is too small
            if nums[a] + sum(nums[-3:]) < target:
                continue
            # a is too large
            if nums[a] + sum(nums[a+1:a+4]) > target:
                break
            prev_b = float("-inf")
            for b in range(a+1, n-2):
                if nums[b] == prev_b:
                    continue
                s = nums[a] + nums[b]
                
                # b is too small
                if s + sum(nums[-2:]) < target:
                    continue
                # b is too large
                if s + sum(nums[b+1:b+3]) > target:
                    break
                
                c = b + 1
                d = n - 1
                
                while c < d:
                    if s + nums[d] + nums[c] < target:
                        while c<n-1 and nums[c+1] == nums[c]:
                            c+=1
                        c+=1
                    elif s + nums[d] + nums[c] > target:
                        while d>1 and nums[d-1] == nums[d]:
                            d-=1
                        d-=1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c<n-1 and nums[c+1] == nums[c]:
                            c+=1
                        while d>1 and nums[d-1] == nums[d]:
                            d-=1
                        c+=1
                        d-=1
                prev_b = nums[b]
            prev_a = nums[a]
        return res                        
        