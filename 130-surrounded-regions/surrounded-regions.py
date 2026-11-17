from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if (i in (0, n -1 ) or j in (0, m - 1)) and board[i][j] == "O":
                    board[i][j] = "S"
                    queue.append((i, j))
                    
        while queue:
            x, y = queue.popleft()
            for a,b in (x + 1, y) , (x - 1, y) , (x, y + 1), (x, y - 1):
                if 0 <= a < n and 0 <= b < m and board[a][b] == "O":
                        board[a][b] = "S"
                        queue.append((a,b))
                       
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"


    