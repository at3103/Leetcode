from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alph = defaultdict()
        retindex=len(s)
        
        l = len(s)
        if not l:
            return -1
        for i in range(l):
            if alph.get(s[i],-1) == -1:
                alph[s[i]] = i
            else:
                alph[s[i]] = l
        retindex = min(alph.values())
        if retindex == l:
            return -1
        return retindex