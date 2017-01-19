class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        cash = 0
        #temp=n
        strt = 0
        end = n
        temp = strt + (end-strt)/2
        while (end-strt)/2:
            cash +=temp
            strt = temp
            temp = strt + (end-strt + 1)/2
        strt = 0
        temp = strt + (end-strt)/2
        while (end-strt)/2:
            cash +=temp
            end = temp
            temp = end - (end-strt)/2
        return cash/2