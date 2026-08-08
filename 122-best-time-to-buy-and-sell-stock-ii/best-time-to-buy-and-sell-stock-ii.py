class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        ans = 0
        a = prices[0]
        for i in range(1,n):
            if prices[i] <= a:
                a =  prices[i]
            else:
                if i < n-1:
                    if prices[i] >= prices[i+1]:
                        ans += prices[i] - a
                        a = prices[i+1]
                else:
                    ans += prices[i] - a
        return ans