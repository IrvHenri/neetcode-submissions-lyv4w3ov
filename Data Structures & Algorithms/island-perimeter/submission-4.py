class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i,j):

            # If you're out of bounds or in water (0) you found an edge, return 1
            if i < 0 or j < 0  or i>= rows or j >= cols or grid[i][j] == 0:
                return 1
            # if you've already visited this square, return 0   
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))
            # find the total of edges in every direction from this square
            perim = dfs(i,j + 1) + dfs(i,j - 1) + dfs(i + 1,j) + dfs(i - 1,j)

            return perim
        
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j]:
                    return dfs(i,j)
        
        return 0
            


        