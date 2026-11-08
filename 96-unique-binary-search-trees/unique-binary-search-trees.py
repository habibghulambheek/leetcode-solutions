class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0:1,1:1, 2:2, 3:5, 4:14, 5:42}
        def helper(n):
            nonlocal dp
            if n in dp:
                return dp[n]
            ans = 0
            for i in range(n):
                ans += helper(i) * helper(n - i - 1)
            dp[n] = ans
            return ans
        return helper(n)
