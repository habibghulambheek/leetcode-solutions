from math import sqrt
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        limit =  int(sqrt(area))
        L,W =None, None
        for i in range(1,limit+1):
            # if area  
            temp_W = i 
            temp_L = area // i
            print(temp_W, temp_L)
            if area  == (temp_L * temp_W):
                L = temp_L
                W = temp_W
        return [L,W]