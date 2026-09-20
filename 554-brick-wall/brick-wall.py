from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        Counter = defaultdict(int)
        n = len(wall[0])
        for row in wall:
            prefix = 0
            n = len(row)
            for i in range(n-1):

                prefix += row[i]
                Counter[prefix] += 1
        n = len(wall)
        ans = n
 
        for item in Counter.items():
            ans = min(n - item[1],ans)
            
        return ans
