"""
This is a program which would convert an integer of base 10 to base 7.
"""
class Solution(object):
    """
    This class contains the soltuion methods.
    """
    @classmethod
    def convert_to_7(cls, num):
        """
        :type num: int
        :rtype: str
        """
        positive_flag = 1
        retstr = ""
        if not num:
            return str(num)
        if num < 0:
            positive_flag = -1
            num *= positive_flag
        while num > 0:
            retstr = str(num%7) + retstr
            num /= 7
        if positive_flag == -1:
            retstr = '-' + retstr
        return retstr
        