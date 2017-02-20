from collections import Counter
import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = Counter(nums)
        
        nums_sorted_dict = sorted(nums_dict.items(), key = operator.itemgetter(1), reverse = True)
        
        return list(map(lambda x: x[0], nums_sorted_dict[:k]))