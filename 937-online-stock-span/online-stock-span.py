class StockSpanner(object):

    def __init__(self):
        # self.span_stack = []
        self.state = []
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # ans = 1
        # for i in range(len(self.state)-1,-1,-1):
        #     if price >=  self.state[i]:
        #         ans += 1
        #     else:
        #         break
        # self.state.append(price)
        # return ans
        # ans = 1
        # # print(self.state)
        # if self.state:
        #     jump = 0
        #     if self.state[-1][0] <= price:
        #         jump = self.state[-1][1] 
        #         ans += jump 
        #     # print(jump)
        #     curr_idx = len(self.state) - jump -1
        #     # print(curr_idx)
        #     while jump != 0 and curr_idx >= 0 and self.state[curr_idx][0] <= price: 
        #         jump = self.state[curr_idx][1] 
        #         ans += jump
        #         curr_idx  -= jump
        # self.state.append((price, ans))))
        ans =  1
        while self.state and self.state[-1][0] <= price:
            ans  += self.state.pop()[1]
        self.state.append((price, ans))
        return ans
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)