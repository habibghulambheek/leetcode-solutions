from collections import deque
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if (i in (0, n -1 ) or j in (0, m - 1)) and grid[i][j] == 1:
                    grid[i][j] = 0
                    queue.append((i, j))
                    
        while queue:
            x, y = queue.popleft()
            for a,b in (x + 1, y) , (x - 1, y) , (x, y + 1), (x, y - 1):
                if 0 <= a < n and 0 <= b < m and grid[a][b] == 1:
                    grid[a][b] = 0
                    queue.append((a,b))

        return sum(map(sum, grid))


