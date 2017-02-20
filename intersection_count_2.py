"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and
the memory is limited such that you cannot load all elements into the memory at once?
"""
from collections import Counter

class Solution(object):
    """
    Class for Solution
    """
    @classmethod
    def intersect(cls, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1_counter = Counter(nums1)
        num2_counter = Counter(nums2)
        intersection_set = set(num1_counter.keys()).intersection(set(num1_counter.keys()))

        intersection_list = []

        for number in intersection_set:
            intersection_count = min([num1_counter[number], num2_counter[number]])
            intersection_list.extend([number] * intersection_count)

        return intersection_list
        