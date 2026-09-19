class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        
        for i in range(len(prices)):
            x = prices[i]
            while stack and prices[stack[-1]] >= x:
                idx = stack.pop()
                prices[idx] -= x
            
            stack.append(i)
        return prices