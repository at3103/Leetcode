"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.

"""
from collections import Counter
class Solution(object):
    """
    Solution class
    """
    @classmethod
    def findKthLargest(cls, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        naive approach
        num_sorted = sorted(nums, reverse = True)
        """

        """
        Priority queue/ bucket sort
        """
        present_count = 0

        nums_counter = Counter(nums)

        nums_sorted = sorted(nums_counter.items(), reverse=True)

        for number, count in nums_sorted:
            if present_count + count >= k:
                return number

            present_count += count

        return nums[0]
        