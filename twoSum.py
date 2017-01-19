'''
Find the index of two integers in a list which sums up to a target
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l =[]
        rem = 0
        for i in xrange(0,len(nums)):
            rem = target - nums[i]
            sub = nums[i+1:]
            if rem in sub:
                l.append(i)
                l.append(sub.index(rem) + i+1)
                break
            
        return l
            
'''        
S = Solution()
print S.twoSum([3,2,4],6)
'''