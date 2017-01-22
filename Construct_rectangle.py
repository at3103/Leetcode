class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        limit  = int(math.sqrt(area))
        for i in range(limit, 0, -1):
            q,r = divmod(area,i)
            if r == 0:
                if i >= q:
                    return [i,q]
                else:
                    return [q,i]
        return []
