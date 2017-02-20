class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        ct = 0

        while ct <  length:
            if not nums[i]:
                del nums[i]
                nums.append(0)
            else:
                i += 1
            ct += 1
            