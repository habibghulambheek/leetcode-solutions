class Solution(object):
    def findMaximizedCapital(self, k, w, profit, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        n  = len(profit)
        capital_profit = [(capital[i], profit[i]) for i in range(n)]
        heapq.heapify(capital_profit)
        profits = []
        while k > 0:
            while capital_profit and capital_profit[0][0] <= w:
                heapq.heappush(profits, -heapq.heappop(capital_profit)[1])
            if not profits:
                break
            w += -heapq.heappop(profits) 
            k -= 1
        return w
