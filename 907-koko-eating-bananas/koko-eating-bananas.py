import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def total_hours(k):
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)
                # print(hours)
            return hours
        left  = 1 
        right = max(piles)
        
        while left <=  right:
            mid = left + (right - left)//2
            hours = total_hours(mid)
            print("mid:", mid)
            print("hours:",hours)
            if hours > h: 
                left = mid + 1
            else:
                right = mid - 1
        return left
                