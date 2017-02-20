"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""
class Solution(object):
    """
    Solution class
    """
    @classmethod
    def remove_element(cls, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count_val = nums.count(val)
        new_length = len(nums) - count_val

        while count_val:
            nums.remove(val)
            nums.append(val)
            count_val -= 1

        return new_length
