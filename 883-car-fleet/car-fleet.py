class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = {}
        n = len(position)
        for i in range(n):
            time[position[i]] = ((target - position[i]) / float(speed[i]))
        position.sort()
        stack = []
        for p in position:
            while stack and time[stack[-1]] <= time[p]:
                stack.pop()
            stack.append(p)
        return len(stack)