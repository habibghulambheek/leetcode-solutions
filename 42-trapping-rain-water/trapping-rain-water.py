class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(height)
        left  = [0]*n
        right = [0]*n
        running_max = 0
        running_idx = -1
        for i in range(n):
            left[i] =  running_idx 
            if running_max < height[i]:
                running_max =  height[i]
                running_idx = i
        running_max = 0
        running_idx = -1
        for i in range(n-1,-1,-1):
            right[i] =   running_idx 
            if running_max < height[i]:
                running_max =  height[i]
                running_idx = i
        water = 0
        # print(left, right)
        i = 0
        while (i < n):
            l =  left[i] 
            r = right[i]
            if l == -1 or r ==  -1 or height[i] >= height[l] or height[i] >= height[r]:
                i +=  1
                continue

            water += min(height[l], height[r]) -  height[i]            
            # print(water)
            i += 1  
        return water