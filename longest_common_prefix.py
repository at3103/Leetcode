"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution(object):
    """
    Class for solution
    """
    @classmethod
    def longestcommonprefix(cls, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if not length:
            return ""
        new_str = '#'.join(strs)
        new_str = '#' + new_str

        for i in range(1, len(strs[0]) + 2):
            if new_str.count(new_str[:i]) != length:
                return new_str[1:i-1]
        return strs[0]
            