class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])

        ans = 0
        n = len(points)
        min_end = points[0][1]
        for i in range(1,n):
            if min_end < points[i][0]:
                 ans += 1
                 min_end = points[i][1]
        return ans+1