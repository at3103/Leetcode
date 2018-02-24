"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        word_set = set(wordDict)
        word_set.add("")
        n = len(s)
        is_possible = [False for i in range(n)]
        is_possible[0] = s[0] in word_set
        for i in range(1, n):
            if (s[:i+1] in word_set):
                    is_possible[i] = True
                    continue
            for j in range(i):
                if (is_possible[j] and s[j+1:i+1] in word_set):
                    is_possible[i] = True
                    break

        return is_possible[n-1]