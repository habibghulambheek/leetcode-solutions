from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        times = [([None] * n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue = deque()
                    queue.append((i, j))
                    times[i][j] = 0
                    while queue:
                        x,y = queue.popleft()
                        for a, b in [(x+1, y), (x-1, y), (x ,y + 1), (x, y - 1)]:
                            if 0 <= a < m and 0 <= b < n and grid[a][b] == 1 :
                                if times[a][b] == None or times[a][b] > (times[x][y] + 1):
                                    times[a][b] = times[x][y] + 1
                                    queue.append((a,b))
        ans = 0
        for i in range(m):
            for j in range(n):
                if times[i][j] != None:
                    ans = max(times[i][j], ans)
                elif grid[i][j] == 1:
                    return -1
        return ans