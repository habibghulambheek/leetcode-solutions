from collections import deque
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0 
        for i in range(n):
            for j in range(m):
                include = True
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    bfs = deque()
                    land = 1
                    bfs.append((i, j))
                    while bfs:
                        x, y = bfs.popleft()
                        for a, b in (x + 1,y), (x - 1,y), (x, y - 1),(x , y + 1):
                            if a >= 0 and a < n and b >= 0 and b < m:
                                if grid[a][b] == 1:
                                    land += 1
                                    grid[a][b] = 0
                                    bfs.append((a, b))
                            else:
                                include = False
     
                    if include:
                        ans += land
                    
        return ans
