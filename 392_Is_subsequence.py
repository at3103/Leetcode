class Solution(object):
	def isSubsequence(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		#Corner Cases and sanity check
		if not s:
			return True
		if not t or len(t) < len(s):
			return False
		j = 0

		for i in t:

		    #if found a common char, increment index of s
			if i == s[j]:
				j+=1

			#if all char of s are present return True
			if j == len(s):
				return True
		return False