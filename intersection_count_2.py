from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
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
        