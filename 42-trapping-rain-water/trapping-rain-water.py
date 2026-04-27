class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # n = len(height)
        # left  = [0]*n
        # right = [0]*n
        # running_max = 0
        # running_idx = -1
        # for i in range(n):
        #     left[i] =  running_idx 
        #     if running_max < height[i]:
        #         running_max =  height[i]
        #         running_idx = i
        # running_max = 0
        # running_idx = -1
        # for i in range(n-1,-1,-1):
        #     right[i] =   running_idx 
        #     if running_max < height[i]:
        #         running_max =  height[i]
        #         running_idx = i
        # water = 0
        # # print(left, right)
        # i = 0
        # while (i < n):
        #     l =  left[i] 
        #     r = right[i]
        #     if l == -1 or r ==  -1 or height[i] >= height[l] or height[i] >= height[r]:
        #         i +=  1
        #         continue

        #     water += min(height[l], height[r]) -  height[i]            
        #     # print(water)
        #     i += 1  
        # return water

        # Monotonic stack approach

        stack = []
        n  = len(height)
        min_border = None
        water = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                v = height[stack.pop()]
                if not stack:
                    break
                # print(stack, height[i])
                min_border = min(height[stack[-1]],height[i])
                width = i - stack[-1] - 1
                water += (min_border - v) * width 
            # print(stack)
            stack.append(i)
        # [0,1,0,2,1,0,1i,3,2,1,2,1]
        # [2,1,1] temp_stack = [0] , 2
        return water