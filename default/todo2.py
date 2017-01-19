class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tempstr = ""
        retlist = []
        l = len(nums)
        templist=[]
        retlist.append(templist)
        for i in range(len(nums)):
            #templist = nums[i]
            retlist.append([nums[i]])
        for tlist in retlist:
            for j in range(1,len(nums)):
                tset = set(tlist)
                tset.add(nums[j])
                if len(tset) > l:
                    break
                retlist.append(list(tset))
                
                # tempstr+= " " + str(nums[j])
                # templist = tempstr.split()
                # retlist.append(templist)    
        
        #retlist = set(retlist)
        #retlist = list(retlist)
        
        return retlist
        