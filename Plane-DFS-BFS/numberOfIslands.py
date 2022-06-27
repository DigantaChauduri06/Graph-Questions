class Solution:
    def numIslands(self, grid) -> int:
        ROW, COL, cnt = len(grid), len(grid[0]), 0
        
        def helper(r, c):
            if r >= ROW or r < 0 or c >= COL or c < 0 or grid[r][c] != '1':
                return
            grid[r][c] = '2'
            helper(r+1, c)
            helper(r-1, c) 
            helper(r, c+1) 
            helper(r, c-1)
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    helper(i, j)
                    cnt += 1
        return cnt