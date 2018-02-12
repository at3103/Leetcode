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

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0
        
        for i,row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    per += int(j-1 < 0) + int(j-1>=0 and (not row[j-1])) 
                    per += int(j+1 >= len(row)) + int(j+1<len(row) and (not row[j+1])) 
                    per += int(i-1 < 0) + int(i-1>=0 and (not grid[i-1][j])) 
                    per += int(i+1 >= len(grid)) + int(i+1<len(grid) and (not grid[i+1][j])) 
                    
        return per                    
