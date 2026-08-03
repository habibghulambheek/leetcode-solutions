class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ans = 1
        n = len(ratings)
        ans =  [0]*n
        ans[0] =  1
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                ans[i] = ans[i-1] + 1
            else:
                ans[i] =  1 
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                if ans[i] < ans[i+1] +1:
                    ans[i] = ans[i+1] + 1
       
        return sum(ans)