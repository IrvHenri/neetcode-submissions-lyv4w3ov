class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col,res = len(grid),len(grid[0]),0


        for i in range(row):
            for j in range(col):
                square = grid[i][j]

                if square == 1:
                    # top
                    res += (i - 1 < 0 or grid[i - 1][j] == 0 )
                    # bottom
                    res += (i + 1 >= row or grid[i + 1][j] == 0 ) 
                    # left 
                    res += (j - 1 < 0 or grid[i][j - 1] == 0 )
                    # right
                    res += (j + 1 >= col or grid[i][j + 1] == 0 )
        return res     
        