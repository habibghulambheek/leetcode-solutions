class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum  = [0] * n
        postfix_sum = [0] * n

        for i in range(n):
            j = (n-1) - i
            if i == 0:
                prefix_sum[i] += nums[i]
            else:
                prefix_sum[i] += prefix_sum[i-1] + nums[i]
            
            if j == n - 1:
                postfix_sum[j] += nums[j]
            else:
                postfix_sum[j] += postfix_sum[j+1] + nums[j]
        ans = 0
        for  i in range(n-1):
            if (prefix_sum[i] - postfix_sum[i+1])%2 == 0:
               ans += 1
        return ans 