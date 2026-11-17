from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        queue = deque()
        seen = set()
        for i in range(n):
            for j in range(m):
                if (i in (0, n -1 ) or j in (0, m - 1)) and board[i][j] == "O":
                    seen.add((i, j))
                    queue.append((i, j))
                    
        while queue:
            x, y = queue.popleft()
            for a,b in (x + 1, y) , (x - 1, y) , (x, y + 1), (x, y - 1):
                if 0 <= a < n and 0 <= b < m and board[a][b] == "O":
                    if (a,b) not in seen:
                        queue.append((a,b))
                        seen.add((a, b))
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen:
                    board[i][j] = "X"


    