"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases.

"""

from collections import defaultdict

class Solution(object):
    def wordPattern(self, pattern, mystr):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = mystr.split()
        
        encountered = set()
        
        pat_dict = defaultdict(str)
        
        if len(words) != len(pattern):
            return False
        
        for i, wrd in enumerate(words):
            
            if wrd in encountered and pat_dict.get(pattern[i],"") != wrd:
                return False
            if wrd not in encountered and pat_dict.has_key(pattern[i]):
                return False
            
            elif wrd not in encountered:
                encountered.add(wrd)
                pat_dict[pattern[i]] = wrd
                
        return True        
        