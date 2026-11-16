from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        n,m =  len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area  = 1
                    bfs = deque()
                    bfs.append((i, j))

                    while bfs:
                        x, y = bfs.popleft()
                        for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x , y -  1)):
                            if a >= 0 and a < n and b >= 0 and b < m and grid[a][b] == 1:
                                grid[a][b] = 0
                                area += 1
                                bfs.append((a,b))
                    ans = max(ans, area)
        return ans
