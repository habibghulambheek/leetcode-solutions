class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bought_stock  = prices[0]
        profit = 0
        n = len(prices)
        for i in range(1,n):
            # print("bought_stock:", bought_stock)
            # print("prices[",i,"]:", prices[i])        
            # print("profit:", profit)        
            
            if bought_stock > prices[i]:
                bought_stock = prices[i]
            else:
                profit = max(profit, prices[i] - bought_stock)
        return profit