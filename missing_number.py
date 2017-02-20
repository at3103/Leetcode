class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        original_sum = sum(range(len(nums) + 1))
        actual_sum = sum(nums)

        return original_sum - actual_sum


class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        original_sum = (length * (length + 1)) /2
        actual_sum = sum(nums)

        return original_sum - actual_sum

