"""
Move the zeroes to the end
"""
class Solution(object):
    """
    class for the solution
    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        count = 0

        while count < length:
            if not nums[i]:
                del nums[i]
                nums.append(0)
            else:
                i += 1
            count += 1
            