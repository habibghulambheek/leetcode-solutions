class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap  = [1]  
        ugly_nums = []
        factors = [2,3,5]
        covered =  {1}
        while len(ugly_nums) < n:
            num = heapq.heappop(heap)
            ugly_nums.append(num)
            # print(ugly_nums)
            for x in factors:
                y = num * x
                if y not in covered:
                    heapq.heappush(heap,y)
                    covered.add(y)
        return ugly_nums[n-1]
