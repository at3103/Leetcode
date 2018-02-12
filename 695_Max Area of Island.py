"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

"""

from collections import defaultdict, deque

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        grid_filled = {(x,y) for x, row in enumerate(grid) for y in range(len(row))  if row[y] == 1 }
        grid_stack = deque()
        max_ar = 0
        
        while grid_filled:
            cur = grid_filled.pop()
            grid_stack.append(cur)    
            ar = 0
            visited = set()
            visited.add(cur)
            while grid_stack:
                x,y = grid_stack.pop()
                ar += 1
                new_grids = set()
                if (x-1,y) in grid_filled and (x-1,y) not in visited:
                    new_grids.add((x-1,y))
                if (x+1,y) in grid_filled and (x+1,y) not in visited:
                    new_grids.add((x+1,y))
                if (x,y-1) in grid_filled and (x,y-1) not in visited:
                    new_grids.add((x,y-1))
                if (x,y+1) in grid_filled and (x,y+1) not in visited:
                    new_grids.add((x,y+1))
                
                grid_stack.extend(new_grids)
                visited.update(new_grids)
                    
            if ar > max_ar:
                max_ar = ar
            grid_filled -= visited
            
        return max_ar            

                
                
        