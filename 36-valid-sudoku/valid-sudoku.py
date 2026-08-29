from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        box  = defaultdict(set)
        n = len(board)
        for i in range(n):
            for j in range(n):
            
                if board[i][j] != ".":
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in box[(i//3, j//3)]:
                        return False
                    box[(i//3, j//3)].add(board[i][j])
                    rows[i].add(board[i][j]) 
            
                if board[j][i] != ".":
                    if board[j][i] in cols[i]:
                        return False
                    cols[i].add(board[j][i]) 
                

        return True
            

