"""
Docstrring for the file
problem 26: Remove duplicates form sorted array
"""
class Solution(object):
    """
    Doc_string for class:
    """
    @classmethod
    def remove_duplicates(cls, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(set(nums))
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i-1]
            else:
                i += 1
        return length

S = Solution()
print S.remove_duplicates([1, 2, 2, 3, 4, 1, 2])
