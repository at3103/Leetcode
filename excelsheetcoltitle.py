class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s =""
        while n:
            if n%26 == 0:
                s = 'Z' + s
                n-=26
            else:    
                s = chr((n%26) + 64) + s
            n/=26
        return s