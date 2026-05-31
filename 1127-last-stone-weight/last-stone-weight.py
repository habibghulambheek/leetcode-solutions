import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones_temp = [-x for x in stones]
        heapq.heapify(stones_temp)
        while len(stones_temp) > 1:
            # print(stones_temp)
            y = -heapq.heappop(stones_temp)
            x = -heapq.heappop(stones_temp)
            if x != y:
                new_stone = y  - x
                heapq.heappush(stones_temp, -new_stone)
        
        if stones_temp:
            return -stones_temp[0]
        return 0