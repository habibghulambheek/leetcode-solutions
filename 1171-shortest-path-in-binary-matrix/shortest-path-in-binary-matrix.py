from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
            n = len(grid)
            queue = deque()
            if grid[0][0]:
                return -1
            if n == 1:
                return 1
            queue.append((0,0, 1))
            grid[0][0] =1
        
            while queue:
                x, y , val = queue.popleft()
                for a, b in [(x + 1, y),(x - 1, y),(x, y + 1), (x, y - 1),(x + 1, y + 1), (x - 1, y -1),(x - 1, y + 1),(x + 1, y - 1)]:
            
                    if 0 <= a < n and 0 <= b < n and grid[a][b] == 0:
                        if a == n-1 and b == n-1:
                            return val + 1
                        grid[a][b] = 1
                        queue.append((a,b, val + 1))
            return -1