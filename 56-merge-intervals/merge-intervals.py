class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key = lambda x: x[0])
        # print(intervals)
        ans = []
        n = len(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,n):
            # print(intervals[i-1], intervals[i])
            # print(start, end)
            if end >= intervals[i][0]:

                end   = max(end,intervals[i][1])
                

            else:
                ans.append([start,end])
                start = intervals[i][0]
                end =  intervals[i][1]
            # print(start, end)

        ans.append([start,end])
        return ans
