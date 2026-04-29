class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack  = []
        n  = len(asteroids)
        for i in range(n):
            flag = True
            if asteroids[i] < 0:
                while stack and flag:
                    if stack[-1] < 0:
                        break
                    mag =  abs(asteroids[i])

                    if stack[-1] < mag:
                        asteriod = stack.pop()
                    elif stack[-1] == mag:
                        asteriod = stack.pop()
                        flag = False
                        break
                    else:
                        flag = False

                    
                        
            if flag:
                stack.append(asteroids[i])
        return stack