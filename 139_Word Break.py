class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return False
        wd = dict()
        for w in wordDict:
            wd[w] = 1
        opt = list()
        for i in range(0,n):
            opt.append(False)
            if wd.get(s[0:i+1]):
                opt[i] = True
                continue
            for j in range(i-1,-1,-1):
                if opt[j]:
                    if wd.get(s[j+1:i+1]):
                        opt[i] = True
                        break
        return opt[n-1]
