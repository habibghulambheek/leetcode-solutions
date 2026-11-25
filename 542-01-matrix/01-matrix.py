from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n, m = len(mat), len(mat[0])
        
        queue = deque()
        seen = set()
        Distances =[[None] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    seen.add((i,j))

        # print(Distances, queue)
        while queue:
                x, y, val = queue.popleft()
                if mat[x][y] == 0:
                    Distances[x][y] = 0 
                for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= i < n and 0 <= j < m and (i, j) not in seen:
                        if mat[i][j] == 1:
                            if Distances[i][j] == None:
                                Distances[i][j] = val + 1
                            queue.append((i, j , val + 1))
                            seen.add((i,j))


        return Distances