from itertools import permutations
from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = ""
        l = range(1,n+1)
        pl=list()
        pl.append(1)
        for i in l[1:]:
            pl.append(factorial(i-1))
        for i in range(len(pl)):
            if pl[i]>k:
                break
        rl = range(n-i,n+1)

        pm = list(permutations(rl,i+1))
        sl = range(1,n-i)
        fh=""
        for i in sl:
            fh+=str(i)
        req = pm[k-1]
        for i in req:
            ret+=str(i)
        return fh+ret