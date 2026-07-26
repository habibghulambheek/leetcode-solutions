class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix[0])
        row_sets = set()
        col_sets = set()
        for i in range(n):
            row_sets = set()
            col_sets = set()
            for j in range(n):
                if matrix[i][j] in row_sets:
                    return False
                if matrix[j][i] in col_sets:
                    return False
                row_sets.add(matrix[i][j])
                col_sets.add(matrix[j][i])    
        return True