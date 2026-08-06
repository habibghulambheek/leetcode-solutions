class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        prev = 0
        # print(intervals)
        ans = 0
        for i in range(1, n):
            if intervals[prev][1] > intervals[i][0]:
                if  intervals[prev][1] > intervals[i][1]:
                    prev = i
                ans += 1
                
            else:
                prev = i
        return ans