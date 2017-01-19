class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        c = 0
        if nums.count(nums[0]) == l:
            return c
        m = min(nums)
        M = max(nums)
        min_nums = -1 * m
        if m <= 0 and M <=0:
            for i in range(len(nums)):
                nums[i]= nums[i] + min_nums +1
        m = min(nums)
        if m <= 0:
            c+=(-1*m) + 1
            fb_index = nums.index(max(nums))
            for i in range(l):
                if i != fb_index:
                    nums[i] += c
        m = min(nums)
        if nums.count(nums[0]) != l:
            return sum(nums) - (l*m) + c
        else:
            return c