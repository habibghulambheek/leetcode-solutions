class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        n,m =  len(grid), len(grid[0])
        def isvalid(i, j):
            nonlocal n, m, grid
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or grid[i][j] == 2:
                return False
            return True
        def helper(i , j):
            nonlocal grid, n, m
            if not isvalid(i, j):
                return 0
            grid[i][j] = 2
            return 1 + helper(i+1, j) + helper(i-1, j)+ helper(i, j+1)+ helper(i, j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(helper(i, j), ans)
        return ans

