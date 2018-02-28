"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
"""

from collections import Counter
from functools import reduce
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = Counter(magazine)
        ransom_dict = Counter(ransomNote)
        return reduce(lambda s,x: s+(mag_dict.get(x[0],0) >= x[1]), Counter(ransomNote).items(),0) == len(ransom_dict)