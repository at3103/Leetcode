def check_palindrome(s):
	return list(s) == list(reversed(s))

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        retlist = []
        tlist = list(s)
        retlist.append(tlist)
        print tlist
        for i in range(len(tlist)):
        	templist=tlist[:i-1]
        	if tlist[i] == tlist[i-1]:
        		j = i
        		while tlist[i] == tlist[i-1] and i < len(tlist)-1:
	        		templist .append(''.join(tlist[i-1:i+1]))
	        		if i < len(tlist)-1:
	        			templist.extend(tlist[i+1:])
	        		retlist.append(templist) 
	        		i+=1
	        	i=j

        return retlist


S = Solution()
print S.partition('aaaacaacc')
print check_palindrome('aba')