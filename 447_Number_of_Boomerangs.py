"""Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

from collections import defaultdict
from functools import reduce

def compute_distance(x,y):

    return (x[0] - y[0])**2 + (x[1] - y[1]) **2 

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        num_boom = 0
        for x in points:
            dist = defaultdict(int)
            for y in points:
                if x == y:
                    continue
                d = compute_distance(x,y)
                dist[d] += 1
            filtered_val = [v for v in dist.values() if v > 1]             
            
            num_boom += reduce(lambda acc, x: acc + (x*(x-1)), filtered_val, 0)
                
        
        return num_boom