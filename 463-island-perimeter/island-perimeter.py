class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def helper(i, j):
            nonlocal grid,n,m
            if i < 0 or i >= n or j < 0 or j >= m:
                return 1
            if grid[i][j] == 2:
                return 0
            if grid[i][j] == 0:
                return 1
            grid[i][j] = 2
            return helper(i+1, j) + helper(i-1, j) + helper(i, j + 1) + helper(i, j - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return helper(i, j)
        return 0