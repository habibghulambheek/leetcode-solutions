class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [(position[i],(target - position[i])/ float(speed[i])) for i in range(len(position))]
        pairs.sort(reverse = True)
        fleet = 0
        last_time = 0
        for p, t in pairs:
            if t > last_time:
                fleet += 1
                last_time = t
        return fleet