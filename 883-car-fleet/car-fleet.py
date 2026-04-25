class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [(p, (target - p) / float(s)) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)        
        fleets = 0
        last_time = 0
    
        for p, t in pairs:
            if t > last_time:
                fleets += 1
                last_time = t
        
        return fleets