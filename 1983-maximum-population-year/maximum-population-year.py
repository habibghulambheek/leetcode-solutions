class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        logs.sort()
        # print(logs)
        n  = len(logs)
        # curr_pop = 1
        # max_pop  = 1
        # # extreme boundary
        # max_year = logs[0][0]
        # boundary = logs[0][0]
        # for i in range(1,n):
        #     if (boundary > logs[i][0]):
        #         curr_pop += 1
        #     if curr_pop > max_pop:
        #         max_pop = curr_pop
        #     if boundary < logs[i][1]:
        #         curr_pop = 1
        #         boundary = logs[i][1]
        # bruute force approach
        # curr_pop = 1
        max_pop = 0
        max_year = logs[0][0]
        for i in range(n):
            curr_pop  = 0
            earliest_year = logs[i][0]

            for j in range(n):
                if logs[i][0] >= logs[j][0] and logs[i][0] <= (logs[j][1] -1):
                    curr_pop += 1
                if  curr_pop > max_pop:
                    max_pop = curr_pop
                    max_year = logs[i][0]
        return max_year