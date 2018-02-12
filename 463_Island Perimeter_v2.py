"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below.
"""

from functools import reduce

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0
        all_val = reduce(lambda acc, x: acc + x, grid, list())
        c = len(grid[0])
        r = len(grid)
        for i, val in enumerate(all_val):
            if val == 1:
                per += int((i%c) == 0) + int((i%c)>0 and (not all_val[i-1])) 
                per += int((i+1)%c == 0) + int(((i+1)%c)>0 and (not all_val[i+1])) 
                per += int(i//c == 0) + int(i//c > 0 and (not all_val[i-c])) 
                per += int(i//c == r-1) + int(i//c < r-1 and (not all_val[i+c])) 

                    
        return per