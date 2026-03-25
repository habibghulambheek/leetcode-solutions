class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []

        n = len(prices)
        # ans = [0] * n
        for j in range(n-1,-1,-1 ):
            while stack and stack[-1] > prices[j]:
                stack.pop()
            # if not stack:
            #     ans[j] = prices[j]
            value = prices[j]
            if stack:
                prices[j] = prices[j] - stack[-1]

            stack.append(value)
        return prices