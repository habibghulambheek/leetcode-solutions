class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        n = len(image[0])
        m = len(image)
        color_change =  image[sr][sc]
        
        def helper(i, j):
            nonlocal color_change, image
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if image[i][j] == color_change:
                image[i][j] = color
            else:
                return 
            helper(i-1, j)
            helper(i+1, j)  
            helper(i, j+1)  
            helper(i, j-1)  
        if color_change == color:
            return image
        helper(sr,sc)
        return image